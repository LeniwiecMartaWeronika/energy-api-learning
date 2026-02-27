from entsoe import EntsoePandasClient
import pandas as pd

client = EntsoePandasClient(api_key='YOUR_SECURITY_TOKEN')

start = pd.Timestamp('20240226', tz='UTC')
end = pd.Timestamp('20240227', tz='UTC')
country_code = 'PL' # Poland

# Fetch Day-Ahead Prices
prices = client.query_day_ahead_prices(country_code, start=start, end=end)
print(prices)
