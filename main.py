
from src.client import Client
import asyncio
import random
from aiomultiprocess import Pool
import time
from asyncio.exceptions import TimeoutError
from colorama import Fore, init
import requests
import json
init()
PU = []
with open('token.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        PU.append(line.strip())

async def main(username):
        try:
            client = Client(use_proxy=True, auth_token=username)
            await client.get_proxy()
            res = await client.login()
            await client.close()
        except Exception as e:
            print(e)
            pass

async def x():
        n = 1
        final = [PU[i * n:(i + 1) * n] for i in range((len(PU) + n - 1) // n )]
        for x in final:
            async with Pool() as pool:
                async for result in pool.map(main,x):
                    continue 

if __name__ == '__main__':
    try:
        asyncio.run(x())
    except Exception as e:
        print(e)
        pass
        
# https://www.myexternalip.com/raw
