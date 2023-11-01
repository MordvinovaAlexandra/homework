from cli import argparser
from services.query_service import query_service


if __name__ == "__main__":
    args = argparser.parse_args()
    print(args)

    query_service(args.item, args.category_name, args.save)