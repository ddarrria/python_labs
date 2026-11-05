import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="command", required=True)

    json_parser = sub.add_parser("json2csv", help="Преобразовать JSON‑файл в формат CSV.")
    json_parser.add_argument("--in", dest="input", required=True, help="Путь к входному JSON‑файлу.")
    json_parser.add_argument("--out", dest="output", required=True, help="Путь к выходному CSV‑файлу.")

    csv_parser = sub.add_parser("csv2json", help="Преобразовать CSV‑файл в формат JSON.")
    csv_parser.add_argument("--in", dest="input", required=True, help="Путь к входному CSV‑файлу.")
    csv_parser.add_argument("--out", dest="output", required=True, help="Путь к выходному JSON‑файлу.")

    xlsx_parser = sub.add_parser("csv2xlsx", help="Преобразовать CSV‑файл в формат XLSX.")
    xlsx_parser.add_argument("--in", dest="input", required=True, help="Путь к входному CSV‑файлу.")
    xlsx_parser.add_argument("--out", dest="output", required=True, help="Путь к выходному файлу Excel XLSX.")

    args = parser.parse_args()

    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError:
        parser.error(f"Файл не найден: {args.input}")
    except ValueError as error:
        parser.error(str(error))

        
if __name__ == "__main__":
    main()