import os
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from utils import find_tables, collect_sop_files, build_hyperlink

# GitHub Repo and Authentication
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = "GenomicDataInfrastructure/standard-operating-procedures"
SOP_PATH = "sops/european-level/"
REVIEW_PERIOD_DAYS = 365  # One year

# Regular expression to match the date in the document history (YYYY.MM.DD)
DATE_REGEX = r"\d{4}\.\d{2}\.\d{2}"

# Function to parse the "Document History" table and extract the last date
def get_last_edit_date(soup: BeautifulSoup) -> datetime:
    """
    Extracts the most recent date from the Document History table.
    
    :param soup: BeautifulSoup object of the parsed SOP content.
    :return: Most recent date (datetime object) or None if no valid date is found.
    """
    # Headers to match the Document History table
    aim_headers = ["Template Version", "Instance Version", "Author(s)", "Description of changes", "Date"]
    tables = find_tables(soup, aim_headers)

    if not tables:
        return None  # No Document History table found

    document_history_table = tables[0]  # Use the first found table (assuming there's only one Document History table)
    rows = document_history_table.find_all('tr')[1:]  # Skip header row

    last_date = None
    for row in rows:
        columns = [col.text.strip() for col in row.find_all('td')]
        if len(columns) != 5:
            continue  # Skip improperly formatted rows

        date_str = columns[4]  # The last column is expected to be the date
        if re.match(DATE_REGEX, date_str):
            last_date = datetime.strptime(date_str, "%Y.%m.%d")

    return last_date

def create_github_issue(sop_file: str, last_edit_date: datetime):
    """
    Creates a GitHub issue for SOP review if it hasn't been reviewed in the last year.
    
    :param sop_file: The SOP file being reviewed.
    :param last_edit_date: The last review date of the SOP.
    """
    url = f"https://api.github.com/repos/{REPO}/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    issue = {
        "title": f"SOP Review Due: {sop_file}",
        "body": f"The SOP `{sop_file}` was last edited on {last_edit_date.date()}. Please review.",
        "labels": ["SOP-Review"]
    }
    response = requests.post(url, json=issue, headers=headers)
    if response.status_code == 201:
        print(f"Issue created for {sop_file}")
    else:
        print(f"Failed to create issue for {sop_file}: {response.status_code}, {response.text}")

def check_existing_github_issues(sop_file: str) -> bool:
    """
    Checks if a GitHub issue already exists for the given SOP file.
    
    :param sop_file: The SOP file to check.
    :return: True if an issue exists, False otherwise.
    """
    url = f"https://api.github.com/repos/{REPO}/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    params = {"state": "open", "labels": "SOP-Review"}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Failed to fetch issues: {response.status_code}, {response.text}")
        return False

    issues = response.json()
    sop_name = os.path.basename(sop_file)
    
    for issue in issues:
        if sop_name in issue['title']:
            return True  # SOP already has an open issue

    return False

def check_sop_reviews():
    """
    Main function to check if SOPs need review and create GitHub issues for those due.
    """
    sop_files = collect_sop_files([SOP_PATH])  # Collect all SOP files from the specified directory

    for sop_file in sop_files:
        with open(sop_file, 'r') as f:
            sop_content = f.read()
            soup = BeautifulSoup(sop_content, 'html.parser')
            last_edit_date = get_last_edit_date(soup)

            # If last edit date exists and more than a year has passed, and no issue already exists
            if last_edit_date and (datetime.now() - last_edit_date).days > REVIEW_PERIOD_DAYS:
                if not check_existing_github_issues(sop_file):
                    create_github_issue(sop_file, last_edit_date)
                else:
                    print(f"Issue already exists for {sop_file}, skipping.")

if __name__ == "__main__":
    check_sop_reviews()
