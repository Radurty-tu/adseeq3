# Cloning the Design Datasheet

This repository includes a short Python script `clone_datasheet.py` that reads
`AE1222II_AircraftDesignDataSheet2025(AutoRecovered).xlsx` and writes a separate
copy `cloned_AE1222II.xlsx`. The original Excel file is left untouched in
accordance with the project instructions found in `group.txt`.

The generated clone **is not tracked in Git**. Run the script locally whenever
you need a fresh copy and avoid committing the resulting `.xlsx` file.

Run the script using:

```bash
python3 clone_datasheet.py
```

This will produce a clone of the datasheet in the working directory. If you need
to edit or complete the datasheet, modify the cloned copy rather than the
original file.
