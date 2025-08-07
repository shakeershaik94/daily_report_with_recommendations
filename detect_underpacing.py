import pandas as pd

df = pd.read_csv("data/campaign_delivery_logs.csv")
latest_date = df['date'].max()
latest_df = df[df['date'] == latest_date]

latest_df['pacing_percent'] = round(latest_df['spend'] / latest_df['budget'] * 100, 2)
underpaced = latest_df[latest_df['pacing_percent'] < 80]

underpaced.to_csv("underpacing_alerts.csv", index=False)
print("Underpacing report generated.")