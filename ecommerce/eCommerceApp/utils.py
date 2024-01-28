from .models import Shop, User
from .serializer import CartDetailSerializer


def confirm_status_update(shop):
    shop.confirm_status = True
    shop.save()
    return shop


def user_update(user):
    user.is_seller = True
    user.save()
    return user


def sum_price(query):
    serialize = CartDetailSerializer(query, many=True).data
    sum_price = 0
    for item in serialize:
        sum_price += item['total_price']

    return sum_price
