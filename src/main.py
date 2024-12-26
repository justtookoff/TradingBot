from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from decouple import Config, RepositoryEnv

import yfinance as yf
import matplotlib.pyplot as plt

def main():
	env_path = '../.env'
	config = Config(RepositoryEnv(env_path))

	api_key = config('TRADING_API_KEY')
	api_secret = config('TRADING_API_SECRET')
	paper_flag = (config('PAPER_FLAG').lower() == 'True')
	
	if paper_flag:
		url = 'https://paper-api.alpaca.markets/v2/account'
	else:
		url = 'https://api.alpaca.markets/v2/account'

	trading_client = TradingClient(api_key, api_secret, paper=paper_flag)

	# Get our account information.
	account = trading_client.get_account()

	# Check if our account is restricted from trading.
	if account.trading_blocked:
		print('Account is currently restricted from trading.')

	# Check how much money we can use to open new positions.
	print('${} is available as buying power.'.format(account.buying_power))


if __name__=="__main__":
	main()

