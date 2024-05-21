import asyncio
import aiohttp

#define la funcion asincronica para hacer solicitudes HTTP
async def fetch(url, session):
    async with session.get(url) as response:
        print(f"Status: {response.status}")
        data = await response.text()
        print(f"Data from {url} fetched")
        return data
#Crea una tarea asincrónica principal que maneje múltiples solicitudes: 
async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        await asyncio.gather(*tasks)
#Ejecutar el programa asincrónico: 
urls = ["https://www.amazon.com"] * 5 # Lista de URLs a consultar

asyncio.run(main(urls))


