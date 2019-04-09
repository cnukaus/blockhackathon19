

--https://cloud.google.com/free/?_ga=2.187918696.-1147851063.1554820811
SELECT trans_down.*
	,RANK() OVER (
		PARTITION BY trans.from_address
		,trans.block_timestamp ORDER BY trans_down.block_timestamp
		) AS rank
	,datetime_diff(cast(trans_down.block_timestamp AS DATETIME), cast(trans.block_timestamp AS DATETIME), hour) AS HoursGap
FROM `bigquery - PUBLIC - data.crypto_ethereum.transactions` AS trans
INNER JOIN `bigquery - PUBLIC - data.crypto_ethereum.transactions` AS trans_down ON trans.from_address = trans_down.from_address
	AND trans_down.to_address NOT IN ('0x314159265dd8dbb310642f98f50c066173c1259b')
	AND (trans_down.block_timestamp > trans.block_timestamp)
WHERE (
		trans.block_timestamp >= '2019-03-01 05:41:19'
		OR (
			trans.block_timestamp >= '2018-03-01 05:41:19'
			AND trans.block_timestamp <= '2018-04-08 05:41:19'
			)
		)
	AND trans.to_address IN ('0x314159265dd8dbb310642f98f50c066173c1259b')

