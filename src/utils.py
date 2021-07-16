import requests
from time import sleep
from pprint import pprint
from cyberpy import Transaction

from config import ACCOUNT_API, LCD_API, WALLET


def get_account_data(address: str, account_api: str = ACCOUNT_API, print_message: bool = False):
    _res = requests.get(f'{account_api}{address}')
    try:
        _account_number = int(_res.json()['account']['account_number'])
        _sequence = int(_res.json()['account']['sequence'])
    except KeyError:
        _account_number = int(_res.json()['account']['base_vesting_account']['base_account']['account_number'])
        _sequence = int(_res.json()['account']['base_vesting_account']['base_account']['sequence'])
    if print_message:
        print(f'address: {address}\naccount number: {_account_number}\nsequence: {_sequence}')
    return _account_number, _sequence


def linking(link_candidates: list, wallet: dict = WALLET, sleep_time: float = 0, print_message: bool = True):
    _account_number, _sequence = get_account_data(wallet['address'])
    _tx = Transaction(
        privkey=wallet['private_key'],
        account_num=_account_number,
        sequence=_sequence,
        fee=0,
        gas=100000+100000*len(link_candidates),
        memo="",
        chain_id="bostrom-testnet-3",
        sync_mode="broadcast_tx_sync",
    )
    for _link_candidate in link_candidates:
        if print_message:
            print(f'cyberLink from {_link_candidate[0]} to {_link_candidate[1]}')
        _tx.add_cyberlink(cid_from=_link_candidate[0], cid_to=_link_candidate[1])

    _pushable_tx = _tx.get_pushable()
    _res = requests.post(url=LCD_API, data=_pushable_tx)
    if print_message:
        pprint(_res.json()['result'])
    sleep(sleep_time)
