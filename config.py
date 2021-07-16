from dotenv import dotenv_values

LCD_API = 'https://rpc.bostromdev.cybernode.ai'
ACCOUNT_API = 'https://lcd.bostromdev.cybernode.ai/cosmos/auth/v1beta1/accounts/'

IPFS_HOST = dotenv_values(".env")['IPFS_HOST']

ADDRESS = dotenv_values(".env")['ADDRESS']
PRIVATE_KEY = bytes.fromhex(dotenv_values(".env")['PRIVATE_KEY'])

WALLET = {'address': ADDRESS,
          'private_key': PRIVATE_KEY}

