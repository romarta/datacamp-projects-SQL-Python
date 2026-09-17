# Start coding here
private_ev_charging = pd.read_csv('private_ev_charging.csv')
public_ev_charging = pd.read_csv('public_ev_charging.csv')
ev_sales = pd.read_csv('ev_sales.csv')

#sales in 2018
ev_sales_2018 = ev_sales[ev_sales['year'] == 2018]['sales'].sum()
print(ev_sales_2018)

# sales by year
sales = ev_sales.groupby("year", as_index=False)["sales"].sum()

#trends
fig, ax = plt.subplots(figsize=(15, 5))

ax.plot(private_ev_charging["year"], private_ev_charging["private_ports"], label="Private ports")
ax.plot(public_ev_charging["year"], public_ev_charging["public_ports"], label="Public ports")
ax.plot(sales["year"], sales["sales"], label="Sales")
ax.legend()
plt.show()

#same trends?
ports = private_ev_charging.merge(public_ev_charging, on ='year')
data = ports.merge(sales, on = "year")

corr = data.corr()
sns.heatmap(corr, annot=True)
plt.show()

trend = "same"