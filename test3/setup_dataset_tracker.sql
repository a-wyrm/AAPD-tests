-- Test Case 3 — Dataset Tracker
-- Run this script to create and populate the two tables, then write your queries.

DROP TABLE IF EXISTS datasets;
DROP TABLE IF EXISTS agencies;

CREATE TABLE agencies (
    agency_id   INTEGER PRIMARY KEY,
    agency_name TEXT NOT NULL
);

CREATE TABLE datasets (
    dataset_id   INTEGER PRIMARY KEY,
    title        TEXT NOT NULL,
    agency_id    INTEGER REFERENCES agencies(agency_id),
    year         INTEGER,
    status       TEXT,          -- 'available', 'at_risk', or 'removed'
    last_checked DATE
);

INSERT INTO agencies (agency_id, agency_name) VALUES
    (1, 'Social Security Administration'),
    (2, 'U.S. Census Bureau'),
    (3, 'Centers for Disease Control and Prevention'),
    (4, 'Department of Labor'),
    (5, 'Department of Education');

INSERT INTO datasets (dataset_id, title, agency_id, year, status, last_checked) VALUES
    (1,  'SSA Disability Benefits by State, 2023',            1, 2023, 'available', '2026-06-01'),
    (2,  'SSDI Beneficiary Counts, 2022',                     1, 2022, 'at_risk',   '2026-06-15'),
    (3,  'SSI Recipients by Age, 2021',                       1, 2021, 'removed',   '2026-05-20'),
    (4,  'American Community Survey Disability Data, 2023',    2, 2023, 'available', '2026-06-10'),
    (5,  'Disability Characteristics, 2022',                  2, 2022, 'at_risk',   '2026-06-18'),
    (6,  'Disability and Health Data System, 2023',           3, 2023, 'available', '2026-06-05'),
    (7,  'BRFSS Disability Module, 2021',                     3, 2021, 'removed',   '2026-04-30'),
    (8,  'Disability Employment Statistics, 2023',            4, 2023, 'available', '2026-06-12'),
    (9,  'Disability Employment Statistics, 2020',            4, 2020, 'at_risk',   '2026-06-14'),
    (10, 'IDEA Part B Child Count, 2022',                     5, 2022, 'available', '2026-06-08'),
    (11, 'IDEA Part C Early Intervention, 2021',              5, 2021, 'at_risk',   '2026-06-16'),
    (12, 'Special Education Expenditures, 2019',              5, 2019, 'removed',   '2026-03-25');
