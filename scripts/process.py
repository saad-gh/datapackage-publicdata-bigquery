import os
import google.cloud.bigquery

# The client library allows to extracts authorization credentials from a json file
# whose path is set as the value of the environment variable "GOOGLE_APPLICATION_CREDENTIALS". This json file
# is readily downloaded when starting a new project in Google's cloud console.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.dirname(os.path.abspath(__file__)) + '\\authCred.json'

# Create a BigQuery client.
bigquery_client = google.cloud.bigquery.Client()

# Query a public dataset.
query = bigquery_client.query("""
#standardSQL
SELECT * FROM publicdata.samples.github_nested LIMIT 5;
""")

# Print out the results.
for row in query.result():
    print(row)