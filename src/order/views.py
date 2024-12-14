# order/views.py

import asyncio
import json

from coin.models import Coin
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .serializers import SubmitOrderSerializer, OrderResponseSerializer


@method_decorator(csrf_exempt, name='dispatch')
class SubmitOrderView(View):
    async def post(self, request, *args, **kwargs):
        try:
            # Decode JSON body asynchronously
            body_unicode = await request.body.decode('utf-8')
            data = json.loads(body_unicode)

            # Initialize serializer with data
            serializer = SubmitOrderSerializer(data)
            if not serializer.is_valid():
                return JsonResponse({'errors': serializer.errors}, status=400)

            validated_data = serializer.validated_data
            coin_symbol = validated_data['coin']
            amount = validated_data['amount']

            # Fetch the coin asynchronously
            try:
                coin = await asyncio.to_thread(Coin.objects.get, symbol=coin_symbol)
            except Coin.DoesNotExist:
                return JsonResponse({'error': f'Coin with symbol "{coin_symbol}" does not exist.'}, status=404)

            # For demonstration, just print the order details
            print(f"Order submitted: Coin={coin.name}, Amount={amount}")

            # Prepare response data using OrderResponseSerializer
            order_data = {
                'coin': coin.name,
                'symbol': coin.symbol,
                'amount': amount
            }
            response_serializer = OrderResponseSerializer(
                message='Order submitted successfully.',
                order_data=order_data
            )
            serialized_response = response_serializer.serialize()

            return JsonResponse(serialized_response, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON.'}, status=400)
        except Exception as e:
            # Log the exception as needed
            return JsonResponse({'error': 'An unexpected error occurred.'}, status=500)
