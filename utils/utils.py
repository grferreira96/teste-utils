from pyspark.sql.functions import col


def xpto(df, column):
    new_df = df.withColumn(column + "n_ew", col(column) + 1)
    return new_df