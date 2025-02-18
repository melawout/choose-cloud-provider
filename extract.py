import requests


def get_jobs_list(url, headers, querystring):
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as http_error_message:
        print(f"❌ [HTTP ERROR]: {http_error_message}")

    except requests.exceptions.ConnectionError as connection_error_message:
        print(f"❌ [CONNECTION ERROR]: {connection_error_message}")

    except requests.exceptions.Timeout as timeout_error_message:
        print(f"❌ [TIMEOUT ERROR]: {timeout_error_message}")

    except requests.exceptions.RequestException as error_message:
        print(f"❌ [ERROR]: {error_message}")
