from src.mysql import create_pool
from src.models import User
import asyncio,sys

loop = asyncio.get_event_loop()
async def test():
    await create_pool(loop=loop,user='root', password='root', database='task')
    u = User(id='ttterer',name = 'myan',email='yanhaaa@111.com',password='Fuck you')
    await u.save()

loop.run_until_complete(test())
loop.close()
if loop.is_closed():
    sys.exit(0)