import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def main():
    parser = argparse.ArgumentParser(description="Extract, transform, and query data")
    parser.add_argument(
        "--extract", action="store_true", help="Perform data extraction"
    )
    parser.add_argument(
        "--load", action="store_true", help="Perform data transformation and loading"
    )
    parser.add_argument(
        "--query", action="store_true", help="Perform data querying"
    )
   
    args = parser.parse_args()

    if args.extract:
        print("Extracting data...")
        extract()

    if args.load:
        print("Transforming data...")
        load()

    if args.query:
        print("Querying data...")
        query()

if __name__ == "__main__":
    main()
