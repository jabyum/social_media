from api import app
from fastapi import Request
from database.postservice import get_exact_hashtag_db, get_some_hashtags_db

@app.get('/api')
async def get_some_hashtags(size: int = 20, page: int = 1):
    if size and page:
        exact_hashtag = get_some_hashtags_db(size)
        return {'status': 1, 'message': exact_hashtag}
    return {'status': 0, 'message': 'wrong data entry'}


@app.get('/api/hastag/<str:hashtag_name>')
async def get_exact_hashtag(request: Request):
    data=await request.json()
    hashtag_name = data.get('hashtag_name')

    if hashtag_name:
        exact_hashtag = get_exact_hashtag_db(hashtag_name)
        return {'status': 1, 'message': exact_hashtag}
    return {'status': 0, 'message': 'wrong data entry'}