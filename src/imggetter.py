import asyncio
import aiohttp
import os
import random
import string


from options import ImageGetterOptions


def generate_random_name(length: int = 10):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length)).lower()


def rename_and_move_folder(source_folder, destination_root):
    if not os.path.exists(source_folder):
        print("Source folder doesn't exist.")
        return
    
    random_name = generate_random_name()
    destination_folder = os.path.join(destination_root, random_name)

    os.rename(source_folder, destination_folder)
    print(f"Folder '{source_folder}' renamed and moved to '{destination_folder}'.")


async def download_random_image(url: str, session: aiohttp.ClientSession):
	async with session.get(url) as response:
		if response.status == 200:
			image_name = generate_random_name() + '.jpg'
			image_path = os.path.join(ImageGetterOptions.DOWNLOAD_DIRECTORY, image_name)
			with open(image_path, 'wb') as f:
				f.write(await response.read())
			print(f"Downloaded: {image_name}")
		else:
			print(f"Failed to download: {url}")
			

async def download_images(url: str):
	async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
		tasks = [download_random_image(url, session) for _ in range(ImageGetterOptions.NUM_IMAGES)]
		await asyncio.gather(*tasks)
       

def main():
    os.makedirs(ImageGetterOptions.DOWNLOAD_DIRECTORY, exist_ok=True)
    os.makedirs(ImageGetterOptions.OLD_IMAGES_DIRECTORY, exist_ok=True)
    rename_and_move_folder(ImageGetterOptions.DOWNLOAD_DIRECTORY, ImageGetterOptions.OLD_IMAGES_DIRECTORY)
    os.makedirs(ImageGetterOptions.DOWNLOAD_DIRECTORY, exist_ok=True)
    asyncio.run(download_images(ImageGetterOptions.UNSPLASH_URL))
    
if __name__ == '__main__':
	main()
