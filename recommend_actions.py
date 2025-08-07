import pandas as pd

df = pd.read_csv("underpacing_alerts.csv")
recommendations = []

for _, row in df.iterrows():
    recs = []
    if row['win_rate'] < 0.4:
        recs.append("Consider increasing bid")
    if row['freq_cap'] <= 3:
        recs.append("Consider relaxing frequency cap")
    recommendations.append("; ".join(recs))

df['recommendations'] = recommendations
df.to_csv("recommendations.csv", index=False)
print("Recommendations file created.")