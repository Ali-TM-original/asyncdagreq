Asyncdagreq --An async api wrapper for Dagpi
==========================================================

`Dagpi <https://dagpi.xyz/>`_

Example:
--------

.. code:: py

    from asyncdagreq import asyncdagreq
    import json

    object = asyncdagreq('your token')

    @bot.command()
    async def roast(ctx):
        roast = await object.roast()
        x = roast.decode("utf-8")
        j = json.loads(x)
        await ctx.send(j['roast'])

    @bot.command()
    async def captcha(ctx):
        url = str(ctx.message.author.avatar_url_as(format="png", static_format="png", size=1024))
        img = await object.captcha(str(url), "hello")
        file = discord.File(img, "pixel.png")
        await ctx.send(file=file)
