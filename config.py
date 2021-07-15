from dotenv import dotenv_values

LCD_API = 'https://rpc.bostromdev.cybernode.ai'
ACCOUNT_API = 'https://lcd.bostromdev.cybernode.ai/cosmos/auth/v1beta1/accounts/'

ADDRESS = dotenv_values(".env")['ADDRESS']
PRIVATE_KEY = bytes.fromhex(dotenv_values(".env")['PRIVATE_KEY'])

WALLET = {'address': ADDRESS,
          'private_key': PRIVATE_KEY}

