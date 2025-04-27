# Databricks notebook source

import dlt

# COMMAND ----------

@dlt.view
def customer_base():
    df_customer = spark.table("bronze.customer")
    df_contact = spark.table("bronze.contact")

    df_customer_with_contact_info = df_customer.alias("customer").join(
        df_contact.alias("contact"),
        don="customer.customer_id = contact.customer_id",
        how="left"
    ).where("customer.is_active = True").select(
        "customer.customer_id",
        "customer.first_name",
        "customer.last_name",
        "customer.registration_date",
        "contact.address",
        "contact.email",
        "contact.phone",
        "contact.preferred_contact_method"
    )

    return df_customer_with_contact_info