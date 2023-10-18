import configuration
import requests
import data
import sender_stand_request


# Дмитрий Кретов, 9-я когорта - Финальный проект, Инженер по тестированию плюс
# Проверка, что по треку заказа можно получить данные о заказе

def test_get_order_by_track():
    track = sender_stand_request.post_new_order(data.order_body).json()["track"]
    act = sender_stand_request.get_order_by_track(track).status_code
    exp = 200
    assert act == 200