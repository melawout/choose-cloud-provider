import pandas as pd

def process_jobs_list(data):

    jobs_list = []

    for job in data["data"]:

        jobs_list.append(
            {
                "job_title": job["job_title"],
                "employer_name": job["employer_name"],
                "job_publisher": job["job_publisher"],
                "job_employment_type": job["job_employment_type"],
                "job_description": job["job_description"],
            }
        )

    return jobs_list


def create_dataframe(data):
    process_list = process_jobs_list(data)
    # print(process_list)

    df = pd.DataFrame(process_list)
    return df
