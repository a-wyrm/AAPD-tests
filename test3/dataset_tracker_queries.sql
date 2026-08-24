-- show every dataset with its full agency name
SELECT d.dataset_id, d.title, a.agency_name, d.year, d.status, d.last_checked FROM datasets AS d
JOIN agencies AS a ON a.agency_id = d.agency_id;


-- datasets currently flagged as 'at_risk' or 'removed', the ones we'd prioritize for preservation
SELECT d.dataset_id, d.title, a.agency_name, d.year, d.status,d.last_checked FROM datasets AS d
JOIN agencies AS a ON a.agency_id = d.agency_id
WHERE d.status IN ('at_risk', 'removed');


-- count datasets per agency and status
SELECT a.agency_name, d.status, COUNT(d.dataset_id) AS dataset_count FROM datasets AS d
JOIN agencies AS a ON a.agency_id = d.agency_id
GROUP BY a.agency_name, d.status
ORDER BY a.agency_name, d.status;
