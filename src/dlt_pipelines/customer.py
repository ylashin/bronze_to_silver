# Databricks notebook source

import dlt
from bronze_to_silver.transformations import add_contact_customer_via
# COMMAND ----------

@dlt.table
def customer():
    df_customer_base = dlt.read("customer_base")
    df_customer = add_contact_customer_via(df_customer_base)
    return df_customer