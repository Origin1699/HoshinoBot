import datetime
import base64
from hoshino import Service
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
from nonebot import MessageSegment, CommandSession, on_command
import pytz

sv = Service('dao', enable_on_default=True, visible=True)

def get_pic(image_path):
    im = Image.open(image_path)  # 打开图像
    width, height = im.size
    ttfont = ImageFont.truetype('hoshino/modules/dao/Deng.ttf', int(height / 18)) #设置字体
    draw = ImageDraw.Draw(im)  # 创建画画对象
    time = datetime.datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%R') #获取当前时间
    draw.text((int(width * 0.40), int(height *0.15)), time, font=ttfont , fill = (20,20,20))  # 添加文字
    return im

def pic2b64(pic:Image) -> str:
    buf = BytesIO()
    pic.save(buf, format='PNG')
    base64_str = base64.b64encode(buf.getvalue()).decode()
    return 'base64://' + base64_str



@on_command("快出刀", aliases=('来催刀了', '几点了', '现在几点了', '报时'), only_to_me=True)
async def dao (session: CommandSession):
    im = get_pic('hoshino/modules/dao/dao.jpg')
    pic = MessageSegment.image(pic2b64(im))
    await session.send(pic)


