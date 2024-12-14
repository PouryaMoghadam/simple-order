from asgiref.sync import sync_to_async
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Coin
from .serializers import CoinSerializer
from ..utils.decorators import async_view


@require_http_methods(["GET"])
@async_view
async def coin_list_view(request):
    try:
        coins_queryset = Coin.objects.all()
        coins = await sync_to_async(list)(coins_queryset)

        if not coins:
            return JsonResponse({"error": "No coins found."}, status=404)

        page = request.GET.get("page", 1)
        page_size = request.GET.get("page_size", 10)

        try:
            page_size = int(page_size)
            if page_size <= 0:
                raise ValueError("page_size must be a positive integer.")
        except ValueError as ve:
            return JsonResponse({"error": str(ve)}, status=400)

        paginator = Paginator(coins, page_size)
        try:
            coins_page = paginator.page(page)
        except PageNotAnInteger:
            coins_page = paginator.page(1)
        except EmptyPage:
            coins_page = paginator.page(paginator.num_pages)

        serializer = CoinSerializer(instance=coins_page, many=True)
        serialized_data = serializer.serialize(request)

        response_data = {
            "count": paginator.count,
            "num_pages": paginator.num_pages,
            "current_page": coins_page.number,
            "results": serialized_data,
        }

        return JsonResponse(response_data, safe=False)
    except ValueError as ve:
        return JsonResponse({"error": str(ve)}, status=400)
    except Exception as e:
        return JsonResponse({"error": "An unexpected error occurred."}, status=500)
