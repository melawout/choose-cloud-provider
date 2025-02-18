import os
from dotenv import load_dotenv
from extract import get_jobs_list
from transform import create_dataframe
from load import load
from check_rate_limit import check_rate_limits


def run_etl():
    load_dotenv()

    url = "https://jsearch.p.rapidapi.com/search"

    api = os.getenv("API_KEY")
    host = os.getenv("API_HOST")

    headers = {"x-rapidapi-key": api, "x-rapidapi-host": host}

    querystring = {
        "query": "cloud engineer in edmonton, alberta",
        "page": "1",
        "num_pages": "10",
        "country": "ca",
        "date_posted": "all",
    }

    # check_rate_limits(url, headers)
    # extract
    jobs_list = get_jobs_list(url, headers, querystring)
    # transform
    df = create_dataframe(jobs_list)
    # load
    load(df)


if __name__ == "__main__":
    run_etl()
