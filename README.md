<div align="center">
  <h1>datafun-02-automation</h1>
  <p><strong>Automate the creation and management of standardized data folders for analytics projects.</strong></p>
</div>

---

## Overview

This project automates the setup of multiple folder structures for organizing data files in Python. It is a fork of the original https://github.com/haileylhanson/datafun-02-automation and expands on the that project initialization to support five folder variations for different data types and organizational needs.

## Features

- Automated creation of standardized, timed, year-based, named, and prefixed folders
- Easy setup and execution
- Designed for data analytics and automation workflows

## Folder Types

- **named_folders/**: Contains folders for different data formats (CSV, Excel, JSON)
- **prefixed_folders_lc/**: Output folders with format prefixes (output--csv, output--excel, output--json)
- **standardized_folders/**: Folders for geographic regions (africa, asia, europe, etc.)
- **timed_folders/**: Folders named by time or sequence (folder_1, folder_2, folder_3)
- **year_folders/**: Folders for each year (2020, 2021, 2022, 2023)

## Requirements

- Python 3.8+
- See `requirements.txt` for dependencies

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/KHenn22/datafun-02-automation.git
   cd datafun-02-automation
   ```
2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   python3 -m pip install --upgrade pip setuptools wheel
   python3 -m pip install -r requirements.txt
   ```

## Usage

To automate folder creation, run:

```bash
python3 dirbot_hennelly.py
```
