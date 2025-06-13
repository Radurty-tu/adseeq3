import openpyxl
from pathlib import Path

SOURCE = Path('AE1222II_AircraftDesignDataSheet2025(AutoRecovered).xlsx')
DEFAULT_TARGET = Path('cloned_AE1222II.xlsx')

def clone_excel(source: Path, target: Path) -> None:
    """Clone an Excel workbook without modifying the source file."""
    wb = openpyxl.load_workbook(source)
    wb.save(target)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Clone the design datasheet")
    parser.add_argument(
        "target",
        nargs="?",
        default=str(DEFAULT_TARGET),
        help="Path for the cloned workbook (default: cloned_AE1222II.xlsx)",
    )
    args = parser.parse_args()

    target = Path(args.target)
    clone_excel(SOURCE, target)
    print(f"Cloned '{SOURCE}' -> '{target}'")
