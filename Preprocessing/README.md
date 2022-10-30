Preprocessing step of the project

I aggregated the unit sales data across all products in each time period at the store level.

Since the data-preprocessing step expects each entry in the timeseries to be a separate row, I first
took the transpose of the original store aggregation dataset. Furthermore, the algorithm expects 
the timeseries to arrive in reverse-chronological order and reverses it during preprocessing. As such, I flip
the data before feeding it into the processed_stock function and save it without the index column.
