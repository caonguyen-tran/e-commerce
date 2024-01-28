from .models import Shop, User


def confirm_status_update(shop):
    shop.confirm_status = True
    shop.save()
    return shop


def user_update(user):
    user.is_seller = True
    user.save()
    return user

