from typing import Tuple, Dict
import requests
import datetime
import pandas as pd

from env import BASE_URL, DISTRIBUTOR_ID


def _generate_headers() -> Dict[str, str]:
    timestamp = (datetime.datetime.now().timestamp() * 1000).__int__()
    return {
        "sfs-distributor-id": DISTRIBUTOR_ID,
        "Authorization": f"Bearer signature=c3RhZ2luZyBzaWduYXR1cmU=,keyId=test-service,timestamp={timestamp}",
    }


def get_daily_stats(
    start_date=datetime.datetime(2023, 1, 1).date(),
    end_date=datetime.datetime.now().date(),
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    data = requests.get(
        f"{BASE_URL}/rest/daily-statistics",
        params={"startDate": start_date.isoformat(), "endDate": end_date.isoformat()},
        headers=_generate_headers(),
    ).json()["data"]

    amounts_dict, counters_dict = data["amounts"], data["counters"]

    amounts_df = pd.DataFrame.from_dict(amounts_dict)
    amounts_df.set_index("date", inplace=True)
    amounts_df.sort_index(inplace=True)
    amounts_df.drop(columns=["currency"], inplace=True)

    counters_df = pd.DataFrame.from_dict(counters_dict)
    counters_df.set_index("date", inplace=True)
    counters_df.sort_index(inplace=True)

    return amounts_df, counters_df
