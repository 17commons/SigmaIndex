import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as pl
from datetime import datetime
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
btcmc = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=90)
ethmc = cg.get_coin_market_chart_by_id(id='ethereum', vs_currency='usd', days=90)
usdtmc = cg.get_coin_market_chart_by_id(id='tether', vs_currency='usd', days=90)
usdcmc = cg.get_coin_market_chart_by_id(id='usd-coin', vs_currency='usd', days=90)
busdmc = cg.get_coin_market_chart_by_id(id='binance-usd', vs_currency='usd', days=90)
daimc = cg.get_coin_market_chart_by_id(id='dai', vs_currency='usd', days=90)
print(btcmc)

fig, ax = plt.subplots()
fig.set_size_inches(8,6)
ax.plot([datetime.utcfromtimestamp(x[0]/1000000) for x in btcmc['market_caps']],
        [x[1] for x in btcmc['market_caps']], label='BTC')
ax.plot([datetime.utcfromtimestamp(x[0]/1000000) for x in ethmc['market_caps'] ],
        [x[1] for x in ethmc['market_caps']], label='ETH')
ax.plot([datetime.utcfromtimestamp(x[0]/1000000) for x in usdtmc['market_caps']],
        [x[1] for x in usdtmc['market_caps']], label='USDT')
ax.plot([datetime.utcfromtimestamp(x[0]/1000000) for x in usdcmc['market_caps']],
        [x[1] for x in usdcmc['market_caps']], label='USDC')
ax.plot([datetime.utcfromtimestamp(x[0]/1000000) for x in busdmc['market_caps']],
        [x[1] for x in busdmc['market_caps']], label='BUSD')
ax.plot([datetime.utcfromtimestamp(x[0]/1000000) for x in daimc['market_caps']],
        [x[1] for x in daimc['market_caps']], label='DAI')
ax.set_xlabel('Hours')
ax.set_ylabel('Price *US$)')
ax.legend();
plt.show()
plt.savefig('/Users/kant/Downloads/20221105-sigmacoingecko/dts.png', format='png')
