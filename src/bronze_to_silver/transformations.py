from pyspark.sql import DataFrame
import pyspark.sql.functions as F

def add_contact_customer_via(df: DataFrame) -> DataFrame:
    
    df = df.withColumn("contact_customer_via", F.expr("""
        CASE
            WHEN preferred_contact_method = 'email' THEN 'Email customer at:' || email
            WHEN preferred_contact_method = 'phone' THEN 'Call customer on:' || phone
            ELSE "unknown"
        END
    """))

    return df