import pandas as pd


def analyze_inventory(file):

    if file is None:
        raise Exception("No file received")

    df = pd.read_csv(file)

    if df.empty:
        raise Exception("Uploaded CSV is empty")

    # clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("Detected columns:", df.columns)

    stock_col = None
    reorder_col = None
    lead_time_col = None

    for col in df.columns:

        if "stock" in col:
            stock_col = col

        if "reorder" in col:
            reorder_col = col

        if "lead_time" in col:
            lead_time_col = col

    if stock_col is None:
        raise Exception("Stock column missing")

    if reorder_col is None:
        raise Exception("Reorder column missing")

    if lead_time_col is None:
        raise Exception("Lead Time column missing")

    # convert numeric safely
    df[stock_col] = pd.to_numeric(df[stock_col], errors="coerce")
    df[reorder_col] = pd.to_numeric(df[reorder_col], errors="coerce")
    df[lead_time_col] = pd.to_numeric(df[lead_time_col], errors="coerce")

    total_products = len(df)

    low_stock = len(df[df[stock_col] <= df[reorder_col]])

    overstock = len(df[df[stock_col] > 150])

    supplier_delay = len(df[df[lead_time_col] > 10])

    return {
        "data": df,
        "total": total_products,
        "low_stock": low_stock,
        "overstock": overstock,
        "supplier_delay": supplier_delay
    }