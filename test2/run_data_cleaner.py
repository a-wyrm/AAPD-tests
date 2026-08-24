import csv, re
from datetime import datetime
from pathlib import Path

# state abbreviations to names
STATE_NAMES = {
	"CA": "California",
	"TX": "Texas",
	"NY": "New York",
	"FL": "Florida",
	"IL": "Illinois",
	"OH": "Ohio",
	"GA": "Georgia",
	"AZ": "Arizona",
	"WA": "Washington",
	"NV": "Nevada",
	"OR": "Oregon",
	"CO": "Colorado",
	"MI": "Michigan",
}

# disability category name changes
DISABILITY_CATEGORIES = {
	"mobility": "Mobility",
	"vision": "Vision",
	"visual": "Vision",
	"hearing": "Hearing",
	"hearing impairment": "Hearing",
	"cognitive": "Cognitive",
	"mental health": "Mental Health",
	"mental-health": "Mental Health",
}


SUPPORTED_DATE_FORMATS = [
    "%Y-%m-%d",
    "%m/%d/%Y",
    "%m-%d-%Y",
    "%Y/%m/%d",
    "%b %d %Y"
]

# function cleans data, takes value and formats it to year, month, day
# if no value, return none
def clean_date(value):
	for date_format in ("%Y-%m-%d", "%m/%d/%Y", "%m-%d-%Y", "%Y/%m/%d", "%b %d %Y"):
		try:
			return datetime.strptime(value.strip(), date_format).strftime("%Y-%m-%d")
		except ValueError:
			continue
	return None


# clean the rows to remove bad data
def clean_row(row):
	# required rows per original dataset
	required_columns = ("record_id", "state", "disability_category", "date_reported", "people_served", "program_status")
	if any(not row.get(column, "").strip() for column in required_columns):
		return None


    # cleans date
	# tries to get the people served
	date_reported = clean_date(row["date_reported"])

    # checks to see if people_served has a value in it, none if not
	try:
		people_served = int(row["people_served"].strip())
	except ValueError:
		people_served = None

	state = row["state"].strip()
	state = STATE_NAMES.get(state.upper(), state.title())
	category_key = re.sub(r"\s+", " ", row["disability_category"].strip().lower())

    # get the disability category from dict
	category = DISABILITY_CATEGORIES.get(category_key)
	status = row["program_status"].strip().title()

    # blank row with nothing
	if not date_reported or people_served is None or not category:
		return None

	return {
		"record_id": row["record_id"].strip(),
		"state": state,
		"disability_category": category,
		"date_reported": date_reported,
		"people_served": str(people_served),
		"program_status": status,
	}


def clean_file(input_path, output_path):
	columns = ["record_id", "state", "disability_category", "date_reported", "people_served", "program_status"]
	cleaned_rows = []

    # dict of row objects to check dups
	seen_rows = set()

	with input_path.open("r", newline="", encoding="utf-8") as input_file:
		for row in csv.DictReader(input_file):
			cleaned_row = clean_row(row)
			if cleaned_row is None:
				continue
			# searches for duplicate columns, if spotted, skip it
			duplicate_key = tuple(cleaned_row[column] for column in columns[1:])
			if duplicate_key in seen_rows:
				continue
			seen_rows.add(duplicate_key)
			cleaned_rows.append(cleaned_row)

    # write to file!
	with output_path.open("w", newline="", encoding="utf-8") as output_file:
		writer = csv.DictWriter(output_file, fieldnames=columns)
		writer.writeheader()
		writer.writerows(cleaned_rows)

	return len(cleaned_rows)


def main():

	data =  Path("./test2/data/messy_disability_services.csv")
	output_path = Path("messy_data_cleaned.csv")
	clean_file(data, output_path)


if __name__ == "__main__":
	main()
