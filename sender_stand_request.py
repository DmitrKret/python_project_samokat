import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


response = post_new_order(data.order_body)


def get_track():
    response = post_new_order(data.order_body)
    return response.json()["track"]


def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS + str(track))