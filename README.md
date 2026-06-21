# Object-Oriented Console Application

A production-ready Python console application built with clean architecture, strict OOP principles, and local JSON database persistence.

## Features
- Complete CRUD actions via memory-to-file mappings.
- Bulletproof validation on data input layers.
- Loose coupling enforced by the Repository Pattern.
- Comprehensive automated Unit Test coverage.

## Architecture & Design Patterns
- **Repository Pattern**: Abstracting data persistence layers out of commercial business logic.
- **Dependency Injection**: Explicit components construction inside the runtime orchestration layer (`main.py`).

## Installation & How to Run
1. Clone the project: `git clone https://github.com`
2. Navigate into root folder: `cd my_console_app`
3. Execute the app: `python main.py`
4. Execute tests: `python -m unittest discover -s tests`

## System Requirements
- Python 3.8 or higher. No external dependencies required.
