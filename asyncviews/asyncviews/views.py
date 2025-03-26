import asyncio
from time import sleep
import httpx
from django.http import HttpResponse

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('''<body id="background" style="background-color:black"> <audio id='sound' src='https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3'> </audio> <h1 style="color:cyan; text-align:center; cursor:pointer">Usando Async Django</h1> <script> document.addEventListener('DOMContentLoaded', function() {const audio = document.getElementById('sound'); document.body.addEventListener('click', function() { if (audio.paused) { audio.play(); setInterval(() => document.getElementById('background').style.backgroundColor = ['green', 'orange', 'blue', 'purple', 'black'][Math.floor(Math.random() * 5)], 50)}}); }); </script> </body>''')