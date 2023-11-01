import csv
from rich.console import Console
from rich.table import Table


def report_cli_adhoc(data: list[dict], columns: list[str]) -> None:
    table = Table(title="Star Wars Movies")

    for column in columns:
        table.add_column(column, justify="cenrer", style="magenta")
    

    for row in data:
        table.add_row(*[row[col] for col in columns])
    

    console = Console()
    console.print(table)

def report_csv_adhoc(data: list[dict], columns: list[str]) -> None:
    with open('report.csv', 'w', encoding="utf-8") as f:
        writer = csv.DictWriter(f, columns)
        writer.writeheader()
        writer.writerows(data)