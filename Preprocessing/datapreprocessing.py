import pandas as pd


data_file = pd.read_csv('/Users/iustintoader/Desktop/Research/CollaborativeForecasting/Coding/preprocessing/sales_train_validation.csv')

print(data_file.head())

print(data_file.shape)

"""Number of NA values"""

print(data_file.isnull().sum().sum())

"""
No NA values

Number of values equal to 0
"""

(data_file==0).sum().sum()

"""Group data by store_id"""

new_df=data_file.groupby("store_id")

new_df_sum = new_df.sum()

"""Check if grouping results in 10 time series, one for each store"""

print(new_df_sum)

"""Results confirmed"""

"""
Since the data-preprocessing step expects each entry in the timeseries to be a separate row, I first
took the transpose of the original store aggregation dataset. Furthermore, the algorithm expects 
the timeseries to arrive in reverse-chronological order and reverses it during preprocessing. As such, I flip
the data before feeding it into the processed_stock function and save it without the index column.
"""

transformed_data=new_df_sum.T.iloc[::-1]

transformed_data.to_csv("/Users/iustintoader/Desktop/Research/CollaborativeForecasting/Coding/store_gan_generation/trans_agg_by_store.csv", index=False)
