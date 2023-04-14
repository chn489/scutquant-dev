from scutquant import data

df = data.get_high_freq_data(adjust="hfq")
df.to_csv("high_freq.csv")
