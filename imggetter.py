import asyncio
import aiohttp
import os
import random
import string

NUM_IMAGES = 25
UNSPLASH_URL = "https://source.unsplash.com/random/1920x1080"

DOWNLOAD_DIRECTORY = 'img'
os.makedirs(DOWNLOAD_DIRECTORY, exist_ok=True)


def generate_random_name(length: int = 10):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


async def download_random_image(url: str, session: aiohttp.ClientSession):
	async with session.get(url) as response:
		if response.status == 200:
			image_name = generate_random_name() + '.jpg'
			image_path = os.path.join(DOWNLOAD_DIRECTORY, image_name)
			with open(image_path, 'wb') as f:
				f.write(await response.read())
			print(f"Downloaded: {image_name}")
		else:
			print(f"Failed to download: {url}")
			

async def download_images(url: str):
	async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
		tasks = [download_random_image(url, session) for _ in range(NUM_IMAGES)]
		await asyncio.gather(*tasks)
       

def main():
    asyncio.run(download_images(UNSPLASH_URL))
    
if __name__ == '__main__':
	main()
