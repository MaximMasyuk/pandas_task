import pyarrow.parquet as pq

df = pq.read_table("yellow_tripdata_2023-01.parquet").to_pandas()

average_passengers_per_train = df["passenger_count"].mean()

average_trip_distance = df['trip_distance'].mean()

average_fare_per_km = df['total_amount'].mean() / (df['trip_distance'] * 1.6).mean()


def payed_by_cash(df):
    total_trips = df["passenger_count"].count()
    cash_payment_trips = df.where(df["payment_type"] == 2)["payment_type"].count()
    percentage_cash_payments = (cash_payment_trips / total_trips) * 100
    print(f"Percentage of trips are payed by cash {percentage_cash_payments:.2f}%")


if __name__ == '__main__':
    print(f"Average number of passengers in one taxi trip: {round(average_passengers_per_train, 2)}")
    print(f"Average trip distance the passengers take: {round(average_trip_distance, 2)}")
    print(f"Aaverage fare amount per km of trip distance: {round(average_fare_per_km, 2)}")

    payed_by_cash(df)
