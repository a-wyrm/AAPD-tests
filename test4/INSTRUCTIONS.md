# Test Case 4 — Merging multiple datasets and exploring the result (Python)

You've been given three related files:

1. `disability_prevalence.csv` — disability prevalence by state.
   Uses **full state names** (e.g., "California").
2. `state_demographics.csv` — general demographics by state.
   Uses **state abbreviations** (e.g., "CA").
3. `state_fips_lookup.csv` — a lookup table matching state names,
   abbreviations, and standard FIPS codes.

Notice that the two data files don't share a common key directly — one uses
full names, the other uses abbreviations — so you'll need the lookup table to
join them. There are also a few states that appear in one file but not the
other.

## Part 1 — Merge
Using pandas, merge the three files into a single analytical dataset with one
row per state, carrying the prevalence figures, the demographic figures, and a
FIPS code. Be deliberate about which type of join you use and how you handle
states that don't match across files.

## Part 2 — Explore (EDA)
Once merged, explore the combined dataset and tell us what's in it. For example:
- summarize the key variables,
- look at how disability prevalence varies across states,
- calculate a derived field or two (e.g., a per-capita rate, or prevalence vs.
  rural population),
- flag any outliers or anything surprising,
- and show a chart or two to illustrate what you found.

A short written summary of what stands out is part of the deliverable.

## What we're looking for
- Whether you inspect the data before merging rather than assuming it's clean
- How you reason about which join to use and what to do with unmatched states
- Whether you notice if the row count does something unexpected after merging
- Correctness of any derived fields
- Whether your exploration surfaces genuinely useful observations, not just
  column descriptions
- Whether the final dataset and analysis are something you could hand to a researcher

Flagging data-quality issues you spot along the way is a good sign.
