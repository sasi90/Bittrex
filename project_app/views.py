import os
import requests
import base64
import json
from logger import trace, exc

ROOT = os.getcwd()

with open(os.path.join(ROOT + '/config/config_url.json'), 'r+') as js:
    js_url = json.dumps(js.read())


class BITTREX_V3:

    @staticmethod
    def read_auth_details():
        try:
            with open(os.path.join(ROOT + '/config/auth.srt'), 'r+') as auth:
                data = auth.read()
                if data:
                    dic = json.loads(base64.b64decode(data))
                    return dic['username'], dic['password']
                else:
                    return [{'message': 'Unexpected internal server error'}, 500]
        except Exception as e:
            exc.exception(f'Error while fetching the user credential: {e}')
            return [{'message': 'Unexpected internal server error'}, 500]

    @staticmethod
    def collect_all_summaries(request_param):
        try:
            if request_param.method == 'GET':
                trace.info("Collecting the market summaries")
                js_data = requests.get(url=f'https://api.bittrex.com/v3/markets/summaries').json()
                return [js_data, None]
            else:
                return [{'message': 'Invalid API Request'}, 400]
        except Exception as e:
            exc.exception(f'Error while collecting the market summaries: {e}')
            return [{'message': 'Unexpected internal server error'}, 500]

    @staticmethod
    def collect_individual_summary(request_param):
        try:
            if request_param.method == 'GET':
                if 'market_symbol' in request_param.args:
                    market_symbol = request_param.args['market_symbol']
                    trace.info(f'Collecting the market summary for "{market_symbol}"')
                    js_data = requests.get(url=f'https://api.bittrex.com/v3/markets/{market_symbol}/summary').json()
                    return [js_data, None]
                else:
                    return [{'message': 'Missing required parameter'}, 400]
            else:
                return [{'message': 'Invalid API Request'}, 400]
        except Exception as e:
            exc.exception(f'Error while collecting the specific market summary: {e}')
            return [{'message': 'Unexpected internal server error'}, 500]
