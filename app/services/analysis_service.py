def get_summary(df):
    return df.describe().to_dict()


def get_correlation(df):
    return df.corr(numeric_only=True).to_dict()


# 🔥 ADD THIS FUNCTION (THIS IS MISSING)
def get_basic_insights(df):
    insights = {}

    insights["num_rows"] = df.shape[0]
    insights["num_columns"] = df.shape[1]

    # Get top category from first categorical column
    cat_cols = df.select_dtypes(include='object').columns
    if len(cat_cols) > 0:
        col = cat_cols[0]
        insights["top_category"] = df[col].value_counts().idxmax()

    return insights