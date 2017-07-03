import requests

yesterday_total_contribution = 12493.18
address = "0xd0a6E6C54DbC68Db5db3A091B171A77407Ff7ccf"


def get_contract(address):                                                                                                            
    contract_url = "https://api.etherscan.io/api?module=contract&action=getabi&address="
    response = requests.get(contract_url + address)                                   
    result = json.loads(response.json()["result"])
    return result


def get_account_value(address):                                                                                                             
    account = "https://api.etherscan.io/api?module=account&action=balance&address="     
    return int(requests.get(account+address).json()["result"]) / 1000000000000000000.0


def get_bitfinex_ticker(ticker):                                                                                                      
    api_url = "https://api.bitfinex.com/v1"                                             
    response = requests.get(api_url+"/pubticker/"+ticker).json()                      
    return response


def get_eth_eth(address, yesterday_total_contribution):
	current_stage_tokens = 2000000
	account_value = get_account_value(address)
	eos_per_eth = current_stage_tokens/(account_value-yesterday_total_contribution) * float(get_bitfinex_ticker("EOSETH")['last_price'])
	return eos_per_eth

print get_eth_eth(address, yesterday_total_contribution)

