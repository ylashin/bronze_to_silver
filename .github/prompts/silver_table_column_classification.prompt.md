- Understand the lineage needed to build the columns in the Databricks DLT table which is a silver layer table.
- Read only Python files to build the context and understanding of the linege.
- Track the lineage back to the source database which is called `bronze_db`.
- For each column, find out the upstream source column or columns used to produce that column.
- Use the `get_bronze_table_column_classifications` MCP tool, find out bronze column classifications for each bronze table involved in building the current DLT table. Pass the table name only to the tool and don't include the bronze database name.
- Produce a report showing each DLT table column and its upstream source column(s).
- In that report, include information about whether the DLT table column is supposed to have a certain classification like PII or similar.
- If the silver column is based off multiple bronze columns, include the classification information for all bronze columns.
- Generate the report in a nicely formatted table with the following columns:
    * Silver column name
    * Lineage information
    * Classification
