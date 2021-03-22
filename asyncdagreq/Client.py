import aiohttp
from .Errors import *
from io import BytesIO

__all__ = ('__version__', 'Asyncdagreq')
__version__ = '1.1.5'

"""
    HOW DOES THIS WORK?
        First the wrapper sends a Header of containing your Token to the Dagpi Server's
        (Creates A SESSION FOR 60SECONDS WHICH SHOULD BE ENOUGH)
        Which is read and authenticated by the server if it is valid :)
        Then the wrapper sends external links such as https://api.dagpi.xyz/data/roast
        As the token is now authenticated the Api sends back a response which can be read
        And converted into Json or other formats for external use
"""


class Asyncdagreq:
    def __init__(self, token: str):
        header = {
            'Authorization': f'{token}'
        }
        self.session = aiohttp.ClientSession(headers=header, timeout=aiohttp.ClientTimeout(total=60))

        self.data_url_roast = 'https://api.dagpi.xyz/data/roast'
        self.data_url_pokemon = 'https://api.dagpi.xyz/data/wtp'
        self.data_url_joke = 'https://api.dagpi.xyz/data/joke'
        self.data_url_fact = 'https://api.dagpi.xyz/data/fact'
        self.data_url_8ball = 'https://api.dagpi.xyz/data/8ball'
        self.data_url_yomama = 'https://api.dagpi.xyz/data/yomama'
        self.data_url_waifu = 'https://api.dagpi.xyz/data/waifu'
        self.data_url_waifu_search = "https://api.dagpi.xyz/waifu"
        self.data_url_pickup = 'https://api.dagpi.xyz/data/pickupline'
        self.data_url_headline = 'https://api.dagpi.xyz/data/headline'
        self.data_url_GTL = 'https://api.dagpi.xyz/data/logo'
        self.data_url_Flag = 'https://api.dagpi.xyz/data/flag'
        self.image_url = 'https://api.dagpi.xyz/image'

    @staticmethod
    async def error_detection(status):
        if status == 403:
            raise Unauthorized()
        elif status == 415:
            raise Filenotappropriate()
        elif status == 413:
            raise Largeimg()
        elif status == 422:
            raise ProcessError()
        elif status == 400:
            raise Connection()
        elif status == 502:
            raise ERROR502()

    async def roast(self):
        # Returns Random Roasts
        # Does not return Json object by default
        async with self.session.get(self.data_url_roast) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        return data

    async def pokemon(self):
        # Returns Random Pokemon
        # Does not return Json object by default
        async with self.session.get(self.data_url_pokemon) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        return data

    async def joke(self):
        # Returns Random Joke
        # Does not return Json object by default
        async with self.session.get(self.data_url_joke) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        return data

    async def fact(self):
        # Returns Random fact
        # Does not return Json object by default
        async with self.session.get(self.data_url_fact) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        return data

    async def ball(self):
        # Returns Random 8ball messages
        # Does not return Json object by default
        async with self.session.get(self.data_url_8ball) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        return data

    async def yomama(self):
        # Returns Random yomama text
        # Does not return Json object by default
        async with self.session.get(self.data_url_yomama) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        return data

    async def randwaifu(self):
        # Returns Random waifu
        # Does not return Json object by default
        async with self.session.get(self.data_url_waifu) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        return data

    # WAIFU SEARCH
    async def waifu_srch(self):
        # Returns Waifu
        # Does not return json object by default
        async with self.session.get(self.data_url_waifu_search) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        return data

    async def pickup(self):
        # Returns Random Pickup line
        # Does not return Json object by default
        async with self.session.get(self.data_url_pickup) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        return data

    async def Headline(self):
        # Returns Random Headline
        # Does not return Json object by default
        async with self.session.get(self.data_url_headline) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        return data

    async def GTL(self):
        # Returns Random Logo
        # Does not return Json object by default
        async with self.session.get(self.data_url_GTL) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        return data

    async def Flag(self):
        # Returns Random Flag
        # Does not return Json object by default
        async with self.session.get(self.data_url_Flag) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        return data

    # IMAGE COMMANDS START FORM HERE ALL RETURN BYTES IO objects
    async def pixel(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/pixel/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def colors(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/colors/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

            byte = BytesIO(data)
            return byte

    async def america(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/america/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def communism(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/communism/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def triggered(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/triggered/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def wasted(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/wasted/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def invert(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/invert/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def sobel(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/sobel/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def hog(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/hog/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def triangle(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/triangle/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def blur(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/blur/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def rgb(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/rgb/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def angel(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/angel/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def satan(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/satan/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def delete(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/delete/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def fedora(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/fedora/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def hitler(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/hitler/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def wanted(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/wanted/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def stringify(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/stringify/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    # DOES NOT WORK
    async def mosiac(self, url: str, pixels: int):
        param = {'url': url,
                 'pixels': pixels}
        async with self.session.get(f'{self.image_url}/mosiac/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def sithlord(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/sith/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def jail(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/jail/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    # WORKS
    async def pride(self, url: str, flag: str = None):
        if flag is None:
            async with self.session.get(f'{self.image_url}/pride/?url={url}&flag=gay') as resp:
                await self.error_detection(resp.status)
                data = await resp.read()
        elif flag is not None:
            async with self.session.get(f'{self.image_url}/pride/?url={url}&flag={flag}') as resp:
                await self.error_detection(resp.status)
                data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def gay(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/gay/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def trash(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/trash/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def deepfry(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/deepfry/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def ascii(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/ascii/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def charcoal(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/charcoal/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def poster(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/poster/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def sepai(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/sepia/?url={url}', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def swirl(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/swirl/?url={url}', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def paint(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/paint/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def night(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/night/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def rainbow(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/rainbow/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def magik(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/magik/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def fiveguyes(self, url: str, url2: str):
        param = {'url': url,
                 'url2': url2}
        async with self.session.get(f'{self.image_url}/5g1g/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def whygay(self, url: str, url2: str):
        param = {'url': url,
                 'url2': url2}
        async with self.session.get(f'{self.image_url}/whyareyougay/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def obama(self, url: str, url2: str):
        param = {'url': url,
                 'url2': url2}
        async with self.session.get(f'{self.image_url}/obama/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def tweet(self, url: str, url2: str, txt: str):
        param = {'url': url,
                 'username': url2,
                 'text': txt}
        async with self.session.get(f'{self.image_url}/tweet/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def yt(self, url: str, url2: str, txt: str, theme: bool = True):
        param = {'url': url,
                 'url2': url2,
                 'text': txt,
                 'dark': theme}
        async with self.session.get(f'{self.image_url}/yt/', parms=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def discord(self, url: str, url2: str, txt: str, theme: bool = True):
        param = {'url': url,
                 'url2': url2,
                 'text': txt,
                 'dark': theme}
        async with self.session.get(f'{self.image_url}/discord/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def retromeme(self, url: str, top_txt: str, botm_txt: str):
        param = {'url': url,
                 'top_text': top_txt,
                 'bottom_text': botm_txt}
        async with self.session.get(
                f'{self.image_url}/retromeme/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def motivational(self, url: str, top_txt: str, botm_txt: str):
        param = {'url': url,
                 'top_text': top_txt,
                 'bottom_text': botm_txt}
        async with self.session.get(
                f'{self.image_url}/motiv/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def captcha(self, url, txt: str):
        param = {'url': url,
                 'text': txt}
        async with self.session.get(f'{self.image_url}/captcha/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def modernmeme(self, url: str, txt: str):
        param = {'url': url,
                 'text': txt}
        async with self.session.get(
                f'{self.image_url}/retromeme/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def burn(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/burn/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def comic(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/comic/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def sketch(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/sketch/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def spin(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/spin/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def dissolve(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/dissolve/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def neon(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/neon/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def petpet(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/petpet/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def freeze(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/freeze/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def earth(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/earth/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def solar(self, url: str):
        param = {'url': url}
        async with self.session.get(f'{self.image_url}/solar/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def thought_image(self, url: str, txt: str):
        param = {'url': url,
                 "text": txt}
        async with self.session.get(f'{self.image_url}/thoughtimage/', params=param) as resp:
            await self.error_detection(resp.status)
            data = await resp.read()

        byte = BytesIO(data)
        return byte

    async def close(self):
        # For Closing The connection
        return await self.session.close()
