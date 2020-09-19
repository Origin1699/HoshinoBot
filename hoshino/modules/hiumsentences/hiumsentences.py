import requests
from hoshino import Service
from hoshino.typing import CommandSession
from nonebot import on_command


@on_command('网抑云时间', aliases=('上号','生而为人','生不出人','网抑云','已黑化'), only_to_me=False)
async def music163_sentences(session: CommandSession):
    resp = requests.get('http://api.heerdev.top/nemusic/random',timeout=5)
    if resp.status_code == requests.codes.ok:
        res = resp.json()
        sentences = res['text']
        await session.send(sentences, at_sender=False)
    else:
        await session.send('上号失败，我很抱歉。查询出错，请稍后重试。', at_sender=True)

@on_command('舔狗语录',aliases=('在吗','她不爱我','我还爱她','她没错','错的是我'), only_to_me=False)
async def tg_sentences(session: CommandSession):
    resp = requests.get('https://api.ixiaowai.cn/tgrj/index.php/?code=json',timeout=5)
    if resp.status_code == requests.codes.ok:
        res = resp.json()
        sentences = res['msg']
        await session.send(sentences, at_sender=False)
    else:
        await session.send('舔而失败，我很抱歉。查询出错，请稍后重试。', at_sender=True)