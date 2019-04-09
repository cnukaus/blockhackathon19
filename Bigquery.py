# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

from bq_helper import BigQueryHelper
bq_assistant = BigQueryHelper("bigquery-public-data", "github_repos")
QUERY = """
        SELECT message
        FROM `bigquery-public-data.github_repos.commits`
        WHERE LENGTH(message) > 6 AND LENGTH(message) <= 20
        LIMIT 2000
        """
bq_assistant.estimate_query_size(QUERY)
bq_assistant.listtables()

# Any results you write to the current directory are saved as output.