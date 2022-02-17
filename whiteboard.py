"""
서브커맨드 만들기
서브커맨드의 서브커맨드도 가능
@bot.group(invoke_without_command = True) # 서브커맨드가 실행될 때는, await 실행이 안됨
async def def1(ctx):
    await ctx.send()..

@def1.command()
async def subdef(stx):
    await ...


Result: !def1 subdef args..
"""

"""
함수 이름을 지을 수 없을 때
@bot.command(name="func", aliases=('calc', 'clc',) @ name param 이용, alias 별칭 literal
async def _func(ctx):
    await ..
    
@bot.command(description="", hidden=True) # help말고 긴 docs 스트링 설명이 필요할 때, hidden= help에만
숨겨지고 기능은 작동
"""