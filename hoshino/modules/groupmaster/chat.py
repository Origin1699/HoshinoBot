import random

from nonebot import on_command

from hoshino import R, Service, priv, util


# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'), only_to_me=True)
async def say_hello(session):
    await session.send('はい！私はいつも貴方の側にいますよ！')


sv = Service('chat', visible=False)

@sv.on_fullmatch(('沙雕机器人', '沙雕機器人'))
async def say_sorry(bot, ev):
    await bot.send(ev, 'ごめんなさい！嘤嘤嘤(〒︿〒)')


@sv.on_fullmatch(('老婆', 'waifu', 'laopo'), only_to_me=True)
async def chat_waifu(bot, ev):
	if random.randint(0, 1) == 1:
		await bot.send(ev, R.img('laopo.jpg').cqcode)
	else:
		await bot.send(ev, R.img('喊谁老婆呢.jpg').cqcode)


@sv.on_fullmatch('老公', only_to_me=True)
async def chat_laogong(bot, ev):
	pic = R.img(f"chieri{random.randint(3, 4)}.jpg").cqcode
	await bot.send(ev, f"给劳资爪巴！\n{pic}", at_sender=True)


@sv.on_fullmatch('mua', only_to_me=True)
async def chat_mua(bot, ev):
	pic = R.img(f"chieri{random.randint(1, 2)}.jpg").cqcode
	await bot.send(ev, R.img(f"走开啦！\n{pic}"), at_sender=True)


@sv.on_fullmatch('来点星奏')
async def seina(bot, ev):
    await bot.send(ev, R.img('星奏.png').cqcode)


@sv.on_fullmatch(('我有个朋友说他好了', '我朋友说他好了', ))
async def ddhaole(bot, ev):
    await bot.send(ev, '那个朋友是不是你弟弟？')
    await util.silence(ev, 30)


@sv.on_fullmatch('我好了')
async def nihaole(bot, ev):
	await bot.send(ev, R.img('已经可以了.jpg').cqcode)
	
@sv.on_fullmatch('日服公告')
async def nihaole(bot, ev):
	await bot.send(ev, 'https://priconne-redive.jp/news/')
@sv.on_fullmatch('台服公告')
async def nihaole(bot, ev):
	await bot.send(ev, 'http://www.princessconnect.so-net.tw/news')


# ============================================ #


@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('确实.jpg').cqcode)


@sv.on_keyword(('会战'))
async def chat_clanba(bot, ctx):
    if random.random() < 0.02:
        await bot.send(ctx, R.img('我的天啊你看看都几度了.jpg').cqcode)


@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.10:
        await bot.send(ctx, R.img('内鬼.png').cqcode)

@sv.on_keyword(('nmsl'))
async def chat_nmsl(bot, ctx):
    if random.random() < 0.10:
        await bot.send(ctx, R.img('nmsl.png').cqcode)

nyb_player = f'''{R.img('newyearburst.gif').cqcode}
正在播放：New Year Burst
──●━━━━ 1:05/1:30
⇆ ㅤ◁ ㅤㅤ❚❚ ㅤㅤ▷ ㅤ↻
'''.strip()

@sv.on_keyword(('春黑', '新黑'))
async def new_year_burst(bot, ev):
    if random.random() < 0.10:
        await bot.send(ev, nyb_player)
