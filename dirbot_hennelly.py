"""
File: dirbot_hennelly.py

Purpose: Automate the creation of project folders 
(and demonstrate basic Python coding skills).

Hint: See the Textbook, Skill Drills, and GUIDES for code snippets to help complete this module.

Author: Kevin Hennelly

"""

#####################################
# Import Modules at the Top
#####################################

# Import from the Python Standard library
import pathlib
import sys      

# Import packages from requirements.txt
import loguru   

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
import utils_hennelly

#####################################
# Configure Logger and Verify
#####################################

logger = loguru.logger
logger.add("project.log", level="INFO", rotation="100 KB") 
logger.info("Logger loaded.")

#####################################
# Declare global variables
#####################################

# Create a project path object for the root directory of the project.
YEAR_ROOT  = pathlib.Path.cwd() / "year_folders"
NAMED_ROOT = pathlib.Path.cwd() / "named_folders"
PREFIXED_LC_ROOT = pathlib.Path.cwd() / "prefixed_folders_lc"
TIMED_ROOT = pathlib.Path.cwd() / "timed_folders"
STANDARD_ROOT = pathlib.Path.cwd() / "standardized_folders"

REGIONS = [
    "North America", 
    "South America", 
    "Europe", 
    "Asia", 
    "Africa", 
    "Oceania", 
    "Middle East"
]

#####################################
# Define Function 1. For item in Range: 
# Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    logger.info("FUNCTION: create_folders_for_range()")
    logger.info(f"PARAMS: start_year={start_year}, end_year={end_year}")

    YEAR_ROOT.mkdir(exist_ok=True)

    if start_year > end_year:  # safety
        start_year, end_year = end_year, start_year

    for y in range(start_year, end_year + 1):
        p = YEAR_ROOT / str(y)
        p.mkdir(exist_ok=True)
        logger.info(f"Created: {p}")
  

  
#####################################
# Define Function 2. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# After everything else is working, 
# add options to force lowercase and remove spaces
#####################################


def create_folders_from_list(folder_list: list) -> None:
    logger.info("FUNCTION: create_folders_from_list()")
    logger.info(f"PARAMS: folder_list={folder_list}")

    NAMED_ROOT.mkdir(exist_ok=True)

    for name in folder_list:
        s = str(name).strip()
        if not s:
            continue
        p = NAMED_ROOT / s
        p.mkdir(exist_ok=True)
        logger.info(f"Created: {p}")

    

  
#####################################
# Define Function 3. List Comprehension: 
# Create a function to create prefixed folders by transforming a list of names 
# and combining each with a prefix (e.g., "output-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'output-') to add to each
#####################################

def create_prefixed_folders_using_list_comprehension(folder_list: list, prefix: str) -> None:
    logger.info("FUNCTION: create_prefixed_folders_using_list_comprehension()")
    logger.info(f"PARAMS: folder_list={folder_list}, prefix={prefix}")

    PREFIXED_LC_ROOT.mkdir(exist_ok=True)

    paths = [
        PREFIXED_LC_ROOT / f"{prefix}-{str(name).strip()}"
        for name in folder_list
        if str(name).strip()
    ]
    for p in paths:
        p.mkdir(exist_ok=True)
        logger.info(f"Created: {p}")
    

#####################################
# Define Function 4. While Loop: 
# Write a function to create folders periodically 
# (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int, count: int = 3) -> None:
    logger.info("FUNCTION: create_folders_periodically()")
    logger.info(f"PARAMS: duration_seconds={duration_seconds}, count={count}")

    import time
    TIMED_ROOT.mkdir(exist_ok=True)

    for i in range(1, count + 1):
        p = TIMED_ROOT / f"folder_{i}"
        p.mkdir(exist_ok=True)
        logger.info(f"Created: {p}")
        if i < count:
            logger.info(f"Waiting {duration_seconds}s…")
            time.sleep(duration_seconds)
    
    

#####################################
# Define Function 5. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# Add options to force lowercase AND remove spaces
#####################################

def create_standardized_folders(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    logger.info("FUNCTION: create_standardized_folders()")
    logger.info(f"PARAMS: to_lowercase={to_lowercase}, remove_spaces={remove_spaces}")

    STANDARD_ROOT.mkdir(exist_ok=True)

    for name in folder_list:
        s = str(name)
        if to_lowercase:
            s = s.lower()
        if remove_spaces:
            s = s.replace(" ", "_")

        p = STANDARD_ROOT / s
        p.mkdir(exist_ok=True)
        logger.info(f"Created: {p}")

    
  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    logger.info("#####################################")
    logger.info("# Starting execution of main()")
    logger.info("#####################################\n")

    logger.info(f"Byline: {utils_hennelly.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using list comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'output-'
    create_prefixed_folders_using_list_comprehension(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Call function 5 to create standardized folders, no spaces, lowercase
    create_standardized_folders(REGIONS, to_lowercase=True, remove_spaces=True)

    logger.info("\n#####################################")
    logger.info("# Completed execution of main()")
    logger.info("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

    


