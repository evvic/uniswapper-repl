import os
import sys

METAMASK_WALLET_ADDY = os.environ['METAMASK_WALLET_ADDY']

METAMASK_PRIVATE_KEY = os.environ['METAMASK_PRIVATE_KEY']

PROVIDER = os.environ['INFURA_PROVIDER']

from uniswap import Uniswap

VERSION = 2

print('uniswapper')
print(METAMASK_WALLET_ADDY, METAMASK_PRIVATE_KEY, PROVIDER)

print(sys.version)

uniswap = Uniswap(address=METAMASK_WALLET_ADDY, private_key=METAMASK_PRIVATE_KEY, version=VERSION, provider=PROVIDER)





