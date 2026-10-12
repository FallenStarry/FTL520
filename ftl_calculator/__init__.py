from mcdreforged.api.command import *
from mcdreforged.api.types import PluginServerInterface
from ftl_calculator.m01 import red, blue

D = {"n": "11", "s": "00", "w": "01", "e": "10"}

def on_load(server: PluginServerInterface, prev):
    builder = SimpleCommandBuilder()
    builder.command('!!ftl <r> <b> <l>', on_ftl)
    builder.arg('r', Integer)
    builder.arg('b', Integer)
    builder.arg('l', Text)
    builder.register(server)

    server.register_help_message('!!ftl <r> <b> <l>', 'FTL-520 珍珠炮编码器')
    server.logger.info('FTL-520 已加载')

def on_ftl(source, ctx):
    r = ctx['r']
    b = ctx['b']
    l = ctx['l'].lower()

    if l not in D:
        source.reply('§c错误：方向必须是 n/e/w/s')
        return

    try:
        rl = red(r)
        bl = blue(b)
    except Exception as e:
        source.reply(f'§c计算出错：{e}')
        return

    result = f"{rl}-{D[l]}-{bl}"
    source.reply(f'§a编码结果：§b§l{result}')