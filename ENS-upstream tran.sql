

--https://cloud.google.com/free/?_ga=2.187918696.-1147851063.1554820811
SELECT trans_up.*
	,trans_down.to_address AS Destination_address
FROM `bigquery - PUBLIC - data.crypto_ethereum.transactions` AS trans
INNER JOIN `bigquery - PUBLIC - data.crypto_ethereum.transactions` AS trans_down ON trans.from_address = trans_down.from_address
	AND (
		trans_down.block_timestamp >= '2019-01-01 05:41:19'
		AND trans_down.block_timestamp <= '2019-04-08 05:41:19'
		)
INNER JOIN `bigquery - PUBLIC - data.crypto_ethereum.transactions` AS trans_up ON trans.from_address = trans_up.to_address
	AND (
		trans_up.block_timestamp >= '2018-12-01 05:41:19'
		AND trans_up.block_timestamp <= '2019-03-08 05:41:19'
		)
WHERE (
		trans.block_timestamp >= '2019-03-01 05:41:19'
		OR (
			trans.block_timestamp >= '2018-03-01 05:41:19'
			AND trans.block_timestamp <= '2018-04-08 05:41:19'
			)
		)
	AND trans.to_address IN ('0x314159265dd8dbb310642f98f50c066173c1259b')

