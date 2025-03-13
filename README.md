# Starting Setup

## Project Structure  
All code should be organized within the `src` folder, while datasets should be placed in the `resources` directory. The main script must contain routines to execute all experiments.

All external dependencies must be listed in the `requirements.txt` file.

All scripts should be placed in the `src` folder, organized into subfolders. Each subfolder should include an empty `__init__.py` file to allow Python to recognize it as a package. You can then import these scripts in the main script using the following syntax:  
`from path.to.the.script import something`

Within the `src` folder, the recommended subfolders are:
- **`data`**: For data loading and processing.
- **`model`**: For the neural network model.
- **`trainer`**: For training and testing routines.
- **`utilities`**: For useful tools related to the project.

This is just a suggested structure—feel free to modify it as needed while maintaining an organized codebase.

The `utilities` folder also contains two utility classes and one configuration function that may be helpful:

- **`logging_config.py`**: Defines the setup for Python logging, which is a more efficient alternative to `print` statements. To use logging, instantiate the logger:
  ```python
  logger = logging.getLogger(__name__)
  ```
  Then, log messages with:
  ```python
  logger.info("message")
  ```

- **`argument_parser.py`**: Defines a command-line argument parser class. Use this to pass arguments to the main script. You can register new commands using:
  ```python
  parser.register_subcommands("command", ["arguments"], ["help"])
  ```
  Then, when executing the main script, specify which function to run along with its parameters:
  ```bash
  python3 src/main.py prepare --input resources/datasets/dataset.csv
  ```
  This runs the `prepare` function with `resources/datasets/dataset.csv` as an input parameter.

- **`config_manager.py`**: Defines JSON parsers designed to read configuration files. This is useful for managing hyperparameters (e.g., model sizes, learning rates) in a structured and readable way.

## Setting Up the Python Virtual Environment  
Create and activate a Python virtual environment:

```bash
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

To run the script, use:

```bash
python3 src/main.py "command" --"argument" "value"
```

For example:

```bash
python3 src/main.py prepare --input resources/datasets/dataset.csv
```

---

## Alternative: Using Docker  
### Building the Docker Image  
To build the Docker image, run:

```bash
docker build -t fl-ids .
```

### Running the Docker Container  
To start the container with an interactive shell while mounting the `src` and `resources` directories (ensure the dataset is inside `resources`), run:

```bash
docker run --rm -it -v $(pwd)/src:/app/src -v $(pwd)/resources:/app/resources:cached fl-ids bash
```

To run the script inside the container, use:

```bash
fl-ids "command" --"argument" "value"
```

For example:

```bash
fl-ids prepare --input resources/datasets/dataset.csv
```