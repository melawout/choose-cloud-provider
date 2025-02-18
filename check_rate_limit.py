import requests


def check_rate_limits(url, headers):
    """Check rate limits for the API"""

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    rate_limits = {
        "requests_limit": response.headers.get("x-ratelimit-requests-limit"),
        "requests_remaining": response.headers.get("x-ratelimit-requests-remaining"),
        "time_before_requests_reset": response.headers.get("x-ratelimit-requests-reset"),
    }

    print(rate_limits)
