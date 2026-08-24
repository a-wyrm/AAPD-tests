# AAPD Disability Data Set Project

This project catalogs disability employment statistics by state, from the year 2023.


## Data

This project uses employment and disability statistics from 2023. See the ```disability_employment_by_state.csv``` for the data. The data is structured as follows:

| Column | Description |
|--------|-------------|
| `state` | U.S. state name |
| `year` | Year of data collection (2023) |
| `labor_force_participation_rate` | Percentage of working-age population participating in the labor force |
| `employment_rate` | Percentage of population that is employed |
| `population_with_disability` | Total count of individuals with disabilities in the state |

### Source

The data was sourced from [```SOURCE_HERE```](https://aapd.com/) from dates 2023 onward.


## How-to-Use

This includes instructions on how to set up the analysis portion of this repo.

### Installation and Setup

First, make sure that Python 3.8 is installed on your computer. Download Python from the official website:

- **Linux:** Python comes pre-installed on most Linux distros. Install via your package manager (e.g., `sudo apt-get install python3`).
- **Windows:** Download [here](https://www.python.org/downloads/windows/)
- **macOS:** Download [here](https://www.python.org/downloads/macos/)

For editors, we recommend **Visual Studio Code**, **PyCharm**, or **Jupyter Notebook**.

- **Visual Studio Code:** Available for [Linux](https://code.visualstudio.com/Download), [Windows](https://code.visualstudio.com/Download), and [macOS](https://code.visualstudio.com/Download)
- **PyCharm:** Download the Community Edition for [Linux](https://www.jetbrains.com/help/pycharm/installation-guide.html#standalone), [Windows](https://www.jetbrains.com/help/pycharm/installation-guide.html#standalone), and [macOS](https://www.jetbrains.com/help/pycharm/installation-guide.html#standalone)
- **Jupyter Notebook:** Install via pip once Python is set up with `pip install jupyter`

### Structure:

The repo structure is organized as follows:

The ```/data``` folder holds the ```.csv``` files for analysis.

```bash
├── data
│   ├── disability_employment_by_state.csv
|   ├── disability_employment_by_state_maine.csv
└── README.md
```


## TODOs:

Below is a checklist of states from which we have successfully collected data, organized alphabetically.

### States with Data Collected 

- [x] Alabama
- [x] Alaska
- [x] Arizona
- [x] Arkansas
- [x] California
- [x] Colorado
- [x] Connecticut
- [x] Delaware
- [x] Florida
- [x] Georgia
- [x] Hawaii
- [x] Idaho
- [x] Illinois
- [x] Indiana
- [x] Iowa
- [x] Maine

### States Still Needed

- [ ] Kansas
- [ ] Kentucky
- [ ] Louisiana
- [ ] Maryland
- [ ] Massachusetts
- [ ] Michigan
- [ ] Minnesota
- [ ] Mississippi
- [ ] Missouri
- [ ] Montana
- [ ] Nebraska
- [ ] Nevada
- [ ] New Hampshire
- [ ] New Jersey
- [ ] New Mexico
- [ ] New York
- [ ] North Carolina
- [ ] North Dakota
- [ ] Ohio
- [ ] Oklahoma
- [ ] Oregon
- [ ] Pennsylvania
- [ ] Rhode Island
- [ ] South Carolina
- [ ] South Dakota
- [ ] Tennessee
- [ ] Texas
- [ ] Utah
- [ ] Vermont
- [ ] Virginia
- [ ] Washington
- [ ] West Virginia
- [ ] Wisconsin
- [ ] Wyoming

# Acknowledgments/References
Thank you Microsoft for sponsoring this project!

# License
This dataset can be used under license [MIT License](https://opensource.org/license/mit/).