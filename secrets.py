# Databricks notebook source
dbutils.widgets.text("principal", defaultValue="")
dbutils.widgets.text("secret-scope", defaultValue=dbutils.secrets.listScopes()[0].name)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Authentication
# MAGIC
# MAGIC - Default Databricks notebook authentication relies on a temporary Databricks personal access token that Databricks automatically generates in the background for its own use. Databricks deletes this temporary token after the notebook stops running.

# COMMAND ----------

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### PutAcls

# COMMAND ----------

from databricks.sdk.service.workspace import AclPermission, PutAcl

print(AclPermission.READ)
print(AclPermission.WRITE)
print(AclPermission.MANAGE)

# COMMAND ----------

r = (
    w.secrets.put_acl(
        scope=dbutils.widgets.get("secret-scope"),
        principal=dbutils.widgets.get("principal"),
        permission=AclPermission.MANAGE,
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### list_acls

# COMMAND ----------

for _ in w.secrets.list_acls(scope=dbutils.secrets.listScopes()[0].name):
    print(_)
