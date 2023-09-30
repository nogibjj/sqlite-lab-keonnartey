import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def main():
    parser = argparse.ArgumentParser(description="Extract, transform, and query data, generate and push")
    parser.add_argument(
        "--extract", action="store_true", help="Perform data extraction"
    )
    parser.add_argument(
        "--load", action="store_true", help="Perform data transformation and loading"
    )
    parser.add_argument(
        "--query", action="store_true", help="Perform data querying"
    )
    parser.add_argument(
        '--generate_and_push', action='store_true', help="Generate and push data"
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

    if args.generate_and_push:
    # Add your code for generating and pushing data here
        print("Generating and pushing data...")
        generate_and_push()

if __name__ == "__main__":
    main()
