import pandas as pd

def total_revenue(df):
    total_revenue = df.groupby('SalesRep')['TotalPrice'].sum().reset_index()
    total_revenue.columns = ['SalesRep', 'Total Revenue']
    
    return total_revenue
data = {
    'SalesRep': ['Alice', 'Bob', 'Clara', 'Alice', 'Bob'],
    'Product': ['ProductA', 'ProductB', 'ProductA', 'ProductB', 'ProductA'],
    'Quantity': [3, 2, 4, 1, 5],
    'TotalPrice': [150, 200, 200, 100, 400]
}

df = pd.DataFrame(data)
total_revenue_df = total_revenue(df)
print(total_revenue_df)
