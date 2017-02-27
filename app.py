#!/usr/bin/env python3
import logging,asyncio

from aiohttp import web
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%d %b %Y %H:%M:%S',
    filemode='w')

def index(req):
    return web.Response(body=b'<h1>Some content here</h1>', content_type='text/html', charset='UTF-8')

async def init(loop):
    app = web.Application(loop = loop)
    app.router.add_route('GET','/',index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 5000)
    logging.info('server started at http://127.0.0.1:5000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()