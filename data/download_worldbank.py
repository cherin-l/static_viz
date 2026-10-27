# getting world bank data
import requests
import pandas as pd
import pycountry

from pathlib import Path

URL = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL"
CACHE = Path("data/world_bank_pop_2005.csv")

def fetch_population(year=2005):
    resp = requests.get(
        URL,
        params={"date": year, "format": "json", "per_page": 500},
        timeout=30,
    )
    resp.raise_for_status()
    meta, records = resp.json()  # first item is paging metadata
    df = pd.DataFrame(
        {
            "iso3": [r["countryiso3code"] for r in records],
            "country": [r["country"]["value"] for r in records],
            "population": [r["value"] for r in records],
        }
    )
    return df.dropna(subset=["population"])


def numeric_to_iso3(code):
    match = pycountry.countries.get(numeric=f"{int(code):03d}")
    return match.alpha_3 if match else None


if CACHE.exists():
    pop = pd.read_csv(CACHE)
else:
    pop = fetch_population(2005)
    CACHE.parent.mkdir(exist_ok=True)
    pop.to_csv(CACHE, index=False)


"""Download 2005 total population from the World Bank API."""
import requests
import pandas as pd

URL = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL"

resp = requests.get(
    URL,
    params={"date": 2005, "format": "json", "per_page": 500},
    timeout=30,
)
resp.raise_for_status()
_, records = resp.json()  # first item is paging metadata

df = pd.DataFrame(
    {
        "iso3": [r["countryiso3code"] for r in records],
        "country": [r["country"]["value"] for r in records],
        "population": [r["value"] for r in records],
    }
).dropna(subset=["population"])

df.to_csv("data/world_bank_pop_2005.csv", index=False)
print(f"Saved {len(df)} rows")

# Join to your gambling data
users = pd.read_csv("data/PopTrendsBData3Aggs.csv", encoding="latin1")
users["iso3"] = users["CountryID"].map(numeric_to_iso3)

by_country = (
    users.groupby("iso3").size().rename("users").reset_index()
    .merge(pop, on="iso3", how="left")
)
by_country["users_per_million"] = by_country["users"] / by_country["population"] * 1e6
print(by_country.sort_values("users", ascending=False).head(20))