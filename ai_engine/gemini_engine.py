def generate_recommendation(df):

    low_stock_items = df[
        df["Stock_Quantity"] < df["Reorder_Level"]
    ]

    if low_stock_items.empty:
        return "All products sufficiently stocked."

    recommendation = "Products needing restock:\n\n"

    for product in low_stock_items["Product_Name"]:
        recommendation += f"• {product}\n"

    return recommendation