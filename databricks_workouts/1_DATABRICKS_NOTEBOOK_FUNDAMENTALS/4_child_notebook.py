# Databricks notebook source
# MAGIC %md
# MAGIC #Creating this child notebook for the demo of calling child notebook from the parent notebook

# COMMAND ----------

dbutils.widgets.text("table_name", "cities")
table_name = dbutils.widgets.get("table_name")
print(f"parameter passed is {table_name}")
spark.sql(f"select * from {table_name}").show(2)

# COMMAND ----------

spark.sql("SELECT current_database()").show()

# COMMAND ----------

spark.sql("SHOW TABLES").show()

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -l /databricks-datasets/airlines
# MAGIC
# MAGIC head /databricks-datasets/airlines/part-00000

# COMMAND ----------

dbutils.notebook.exit("success")

