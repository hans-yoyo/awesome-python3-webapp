'url handlers'

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    print('*'*20)
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }
