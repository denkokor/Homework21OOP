from entity.request import Request

from entity.courier import Courier
from entity.shop import Shop
from entity.store import Store
from exceptions import InvalidRequest, BaseError, InvalidStorageName

store = Store(items={
    "печенька": 25,
    "собачка": 25,
    "елка": 25,
    "пончик": 3,
    "зонт": 5,
    "ноутбук": 1
})
shop = Shop(items={
    "печенька": 2,
    "собачка": 2,
    "елка": 2,
    "пончик": 1,
    "зонт": 1
})

storages = {
    'магазин': shop,
    'склад': store
}

def main():
    print('\nДобрый день\n')

    while True:

        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')

        user_input = input(
            'Введите запрос в формате "Доставить 3 печенька из склад в магазин"\n'
            'Введите "стоп" или "stop", если хотите закончить:\n'
        )

        if user_input in ('stop', 'стоп'):
            break
        try:
            request = Request(request=user_input, storages=storages)
        except (InvalidRequest, InvalidStorageName) as error:
            print(error.message)
            continue

        courier = Courier(
            request=request,
            storages=storages,
        )

        try:
            courier.move()
        except BaseError as error:
            print(error.message)



if __name__ == '__main__':
    main()









