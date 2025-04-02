import os


def create_file(path, content=""):
    """Creates a file with specified content."""
    with open(path, 'w') as f:
        f.write(content)


def setup_fastapi_project(root):
    """Sets up a FastAPI project structure."""
    # Define the folder structure
    folders = [
        f"{root}/app",
        f"{root}/app/models",
        f"{root}/app/routers",
        f"{root}/app/services",
        f"{root}/app/repositories",
        f"{root}/app/schemas",
        f"{root}/app/utils",
    ]

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Core files
    create_file(f"{root}/app/__init__.py")
    create_file(f"{root}/app/main.py", 'from fastapi import FastAPI\n\napp = FastAPI()')
    create_file(f"{root}/app/config.py", 'import os\n\n# Configuration settings\n')
    create_file(f"{root}/.env", "# Environment variables\n")
    create_file(f"{root}/requirements.txt", "fastapi\nuvicorn\npydantic\n")
    create_file(f"{root}/README.md", "# Project Documentation\n\n## Setup\n\nInstructions go here.")

    # Initial __init__.py files in each directory
    init_folders = ["models", "routers", "services", "repositories", "schemas", "utils"]
    for folder in init_folders:
        create_file(f"{root}/app/{folder}/__init__.py")

    # Example files in each folder
    create_file(f"{root}/app/models/user.py", "class User:\n    pass  # Define user model here\n")
    create_file(f"{root}/app/routers/user.py", "from fastapi import APIRouter\n\nrouter = APIRouter()\n")
    create_file(f"{root}/app/services/user_service.py", "# Business logic goes here\n")
    create_file(f"{root}/app/repositories/user_repo.py", "# Database operations\n")
    create_file(f"{root}/app/schemas/user_schema.py", "# Pydantic models for validation\n")
    create_file(f"{root}/app/utils/hashing.py", "# Utility functions, e.g., for hashing\n")

    print(f"FastAPI project structure created at {root}")


# Run the setup function with desired root folder
# C:\Users\OFS3KOR\PycharmProjects\PythonFastAPIELK
current_directory = os.getcwd()

setup_fastapi_project(current_directory)
