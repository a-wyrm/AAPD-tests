# relational diagram

```mermaid
erDiagram
    AGENCIES ||--o{ DATASETS : publishes
    DATASETS ||--o{ DATASET_RELEASES : has

    AGENCIES {
        INTEGER agency_id PK
        TEXT agency_name
    }

    DATASETS {
        INTEGER dataset_id PK
        INTEGER agency_id FK
        TEXT title
    }

    DATASET_RELEASES {
        INTEGER release_id PK
        INTEGER dataset_id FK
        INTEGER year
        TEXT status
        DATE last_checked
        TEXT website_name
        TEXT source_url
    }
```

- `DATASETS` stores the stable identity of a dataset. 
- `DATASET_RELEASES` stores each yearly release, including its current preservation status and verification details.
    - `release_id` would be a UTC key.
