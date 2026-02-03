# Databricks notebook source
# COMMAND ----------
# Copy dbt docs to DBFS
%sh
RUN_ID=$(date +%Y%m%d_%H%M%S)
databricks fs cp -r /Workspace/Repos/my_repo/dbt_project/target \
                 dbfs:/mnt/dbt_docs/dbt_sql_job/$RUN_ID/

