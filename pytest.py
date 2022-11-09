import matplotlib.pyplot as plt
from datetime import datetime
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
btcmc = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=90)
ethmc = cg.get_coin_market_chart_by_id(id='ethereum', vs_currency='usd', days=90)
usdtmc = cg.get_coin_market_chart_by_id(id='tether', vs_currency='usd', days=90)
usdcmc = cg.get_coin_market_chart_by_id(id='usd-coin', vs_currency='usd', days=90)
busdmc = cg.get_coin_market_chart_by_id(id='binance-usd', vs_currency='usd', days=90)
daimc = cg.get_coin_market_chart_by_id(id='dai', vs_currency='usd', days=90)
hivemc = cg.get_coin_market_chart_by_id(id='hive', vs_currency='usd', days=90)
steemmc = cg.get_coin_market_chart_by_id(id='steem', vs_currency='usd', days=90)
fig, ax = plt.subplots()
fig.set_size_inches(8,6)
ax.plot([datetime.utcfromtimestamp(x[0]/1000) for x in hivemc['prices']],
        [x[1] for x in hivemc['prices']], label='HIVE')
ax.plot([datetime.utcfromtimestamp(x[0]/1000) for x in steemmc['prices'] ],
        [x[1] for x in steemmc['prices']], label='STEEM')
ax.set_xlabel('Hours')
ax.set_ylabel('Price *US$)')
ax.legend();
plt.show
