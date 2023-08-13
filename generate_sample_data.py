import pandas as pd
import numpy as np
import random
import datetime

# Generate sample data
num_entries = 100
products = ['IPhone', 'Macbook Air', 'Apple Watch Ultra']
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 8, 30)

data = []
for _ in range(num_entries):
    product = random.choice(products)
    date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))
    revenue = round(random.uniform(100, 1000), 2)
    data.append((date, product, revenue))

# Create DataFrame
columns = ['Date', 'Product', 'Revenue']
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('sample_sales_data.csv', index=False)