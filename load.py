def load(df, file_path="data.csv"):
    if df is None or df.empty:
        print("No data to save")
        return

    try:
        df.to_csv(file_path, index=False)
        print(f"Data successfully saved {file_path}")
    except Exception as e:
        print(f"error during data saving: {e}")
