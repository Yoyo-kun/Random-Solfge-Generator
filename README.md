# Random Solfège Generator

This project is used to generate random solfège (singing names) to aid in memorization. You can click buttons within the project to trigger the corresponding audio files.

To generate the executable file (which will be saved in the `dist` folder), run the following Python command:

```bash
pyinstaller --onefile --noconsole --icon="NERV.ico" --add-data "Solfège/piano_C4.wav;Solfège" --add-data "Solfège/piano_D4.wav;Solfège" --add-data "Solfège/piano_E4.wav;Solfège" --add-data "Solfège/piano_F4.wav;Solfège" --add-data "Solfège/piano_G4.wav;Solfège" --add-data "Solfège/piano_A4.wav;Solfège" --add-data "Solfège/piano_B4.wav;Solfège" Random_Solfège_Generator.py
```

If an error occurs because the `distutils` module is not installed, it is likely because Python 3.12 has deprecated and removed `distutils` from the standard library, migrating it to `setuptools`. In Python 3.12, you may need to manually install `setuptools` or update related dependencies.

### Fixing the Python SDK Error

If you encounter an error message such as:

`Unable to set Python SDK for Python 3.12 (Random Solfège Generator) (C:/Users/.../Random Solfège Generator/.venv/Scripts/python.exe). This SDK seems invalid.`

You can resolve it by following these steps:

1. **Install `setuptools`**

You can try installing or updating `setuptools` using `pip` to replace the functionality of `distutils`.

Run the following commands in your terminal:

To install `setuptools`:

```bash
pip install setuptools
```

Or, to upgrade an existing `setuptools` installation:

```bash
pip install --upgrade setuptools
```

2. **Use `ensurepip` to Fix `pip`**

If you still encounter issues while installing `setuptools`, you can try using Python’s built-in `ensurepip` tool to repair `pip`.

Run this command in your terminal:

```bash
python -m ensurepip --upgrade
```

This will install or upgrade both `pip` and `setuptools`.
