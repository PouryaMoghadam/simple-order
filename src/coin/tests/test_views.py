import pytest

from src.coin.tests.factories import CoinFactory


@pytest.mark.django_db
class TestCoinListView:
    url = "/api/coin/"

    @pytest.mark.asyncio
    async def test_no_coins_found(self, async_client):

        response = await async_client.get(self.url)
        assert response.status_code == 404
        assert response.json() == {"error": "No coins found."}

    @pytest.mark.asyncio
    async def test_invalid_page_parameter(self, async_client):
        CoinFactory.create_batch(5)
        response = await async_client.get(self.url, {"page": "-1"})
        assert response.status_code == 200
        data = response.json()
        assert data["current_page"] == 1

    # @pytest.mark.asyncio
    # async def test_invalid_page_size_parameter(self, async_client):
    #     # Create some coins
    #     CoinFactory.create_batch(5)
    #     response = await async_client.get(
    #         reverse("coin_list_view"), {"page_size": "invalid"}
    #     )
    #     # Should raise ValueError, returning 400
    #     assert response.status_code == 400
    #     assert "error" in response.json()
    #
    # @pytest.mark.asyncio
    # async def test_unexpected_error(self, async_client):
    #     with patch(
    #         "coin.views.Coin.objects.all", side_effect=Exception("Unexpected Error")
    #     ):
    #         response = await async_client.get(reverse("coin_list_view"))
    #         assert response.status_code == 500
    #         assert response.json() == {"error": "An unexpected error occurred."}
