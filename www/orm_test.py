import orm

from models import User
import asyncio

def test(loop):
    print('test start')
    yield from orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='root', db='py_awesome')
    # yield from orm.create_pool(loop=loop, user='root', password='root', db='py_awesome')
    print('test start - step 2')
    user = User(name='Hyman', email='hyman213@163.com', passwd='123456', image='about:blank')
    print('test start - step 3')
    yield from user.save()


loop = asyncio.get_event_loop()

for x in test(loop):
    pass