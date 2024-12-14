class CoinSerializer:
    """
    Serializer for Coin model instances.
    """

    def __init__(self, instance=None, many=False):
        self.instance = instance
        self.many = many
        self.data = []

    def serialize(self, request):
        if self.many:
            self.data = [
                self._serialize_single(coin, request) for coin in self.instance
            ]
        else:
            self.data = self._serialize_single(self.instance, request)
        return self.data

    @staticmethod
    def _serialize_single(coin, request):
        return {
            "id": coin.id,
            "name": coin.name,
            "symbol": coin.symbol,
            "last_price": str(coin.last_price),
            "image_url": (
                request.build_absolute_uri(coin.image.url) if coin.image else None
            ),
        }
