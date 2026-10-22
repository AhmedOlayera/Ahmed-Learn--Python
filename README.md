# Ahmed-Learn--Python
to Write a CLI that accepts arguments, validates them, and returns proper exit codes.
# Python CLI Calculator

**Powered by JUGGERNAUT TECHNOLOGY SOLUTIONS**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-green)

## 1. Project Overview

The **Python CLI Calculator** is a command-line application designed to perform basic arithmetic operations while demonstrating fundamental software engineering practices.

The application is intended to be shell-agnostic, allowing users to execute it from compatible terminal environments, including PowerShell, Bash, Zsh, and Command Prompt.

This project is the first exercise in the **60 Python Engineering Drills** training program developed under JUGGERNAUT TECHNOLOGY SOLUTIONS.

### Project Objectives

The primary objectives are to:

* Understand how Python applications receive command-line arguments.
* Implement input parsing and validation.
* Perform deterministic arithmetic operations.
* Handle invalid inputs and calculation errors.
* Return meaningful process exit codes.
* Write automated tests using pytest.
* Manage source code using Git and GitHub.
* Learn basic Python packaging and distribution.
* Apply foundational secure coding practices.

---

## 2. Planned Features

The application will support the following features:

| Feature                | Description                                         | Status  |
| ---------------------- | --------------------------------------------------- | ------- |
| Command-line arguments | Receive operands and operators through the terminal | Planned |
| Addition               | Add two numbers                                     | Planned |
| Subtraction            | Subtract two numbers                                | Planned |
| Multiplication         | Multiply two numbers                                | Planned |
| Division               | Divide two numbers                                  | Planned |
| Input validation       | Reject invalid arguments                            | Planned |
| Error handling         | Handle calculation and input errors                 | Planned |
| Exit codes             | Return success and failure statuses                 | Planned |
| Automated testing      | Verify application behavior with pytest             | Planned |
| Shell compatibility    | Support common terminal environments                | Planned |
| Packaging              | Make the calculator installable                     | Planned |

---

## 3. Technology Stack

| Technology              | Purpose                                         |
| ----------------------- | ----------------------------------------------- |
| Python 3.10+            | Application development                         |
| VS Code                 | Development environment                         |
| Git                     | Version control                                 |
| GitHub                  | Repository hosting                              |
| pytest                  | Automated testing                               |
| Python standard library | Argument handling and application functionality |

### Python Concepts

The project will introduce:

* `sys.argv`
* Variables and data types
* Lists
* Conditional statements
* Functions
* Type conversion
* Exception handling
* Standard output and standard error
* Process exit codes

---

## 4. Project Structure

The initial project structure is:

```text
python-cli-calculator/
│
├── calculator.py
│
├── tests/
│
├── README.md
│
└── .gitignore
```

As the project develops, the structure may expand to include:

```text
python-cli-calculator/
│
├── calculator.py
│
├── tests/
│   └── test_calculator.py
│
├── pyproject.toml
│
├── README.md
│
└── .gitignore
```

### File Responsibilities

**calculator.py**

Contains the calculator's command-line interface, validation, and arithmetic functionality.

**tests/**

Contains automated tests for the calculator.

**pyproject.toml**

Will contain Python project configuration and packaging metadata.

**README.md**

Provides project documentation, usage instructions, and development guidance.

**.gitignore**

Specifies files and directories that Git should not track.

---

## 5. Installation and Setup

### Prerequisites

Before starting, ensure you have:

* Python 3.10 or later
* Visual Studio Code
* Git
* A terminal such as PowerShell, Bash, or Zsh

### Step 1: Clone the Repository

Once the project has been published to GitHub, clone it using its actual repository URL.

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd python-cli-calculator
```

Alternatively, create the project directory locally in VS Code.

### Step 2: Verify Python Installation

```bash
python --version
```

On some systems, Python may be available through `python3` instead of `python`.

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS Bash or Zsh:**

```bash
source .venv/bin/activate
```

Virtual environment activation is shell-specific, but the calculator itself is intended to remain shell-agnostic.

---

## 6. Usage

The following examples describe the **intended application behavior** once implementation is complete.

### General Syntax

```bash
python calculator.py <number1> <operator> <number2>
```

### Addition

```bash
python calculator.py 5 + 10
```

Expected output:

```text
15
```

### Subtraction

```bash
python calculator.py 20 - 8
```

Expected output:

```text
12
```

### Multiplication

```bash
python calculator.py 6 "*" 7
```

Expected output:

```text
42
```

### Division

```bash
python calculator.py 20 / 4
```

Expected output:

```text
5
```

**Note:** Quoting the multiplication operator helps prevent shell-specific wildcard expansion.

---

## 7. Input Validation

The calculator must validate arguments before performing arithmetic operations.

### Validation Requirements

1. Exactly three calculator arguments must be provided.
2. The first operand must represent a valid number.
3. The operator must be supported.
4. The second operand must represent a valid number.
5. Division by zero must be rejected.
6. Invalid input must not cause an uncontrolled application crash.

### Supported Operators

| Operator | Operation      |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |

### Invalid Input Examples

**Invalid number:**

```bash
python calculator.py hello + 10
```

Expected behavior:

```text
Error: operands must be valid numbers.
```

**Unsupported operator:**

```bash
python calculator.py 5 invalid 10
```

Expected behavior:

```text
Error: unsupported operator.
```

**Division by zero:**

```bash
python calculator.py 10 / 0
```

Expected behavior:

```text
Error: division by zero is not allowed.
```

---

## 8. Exit Codes

The application must communicate execution outcomes through process exit codes.

| Exit Code | Meaning                           |
| --------- | --------------------------------- |
| `0`       | Successful execution              |
| `1`       | Validation or calculation failure |

### Success Example

```bash
python calculator.py 5 + 10
```

Expected output:

```text
15
```

Expected exit code:

```text
0
```

### Failure Example

```bash
python calculator.py 5 + hello
```

Expected error:

```text
Error: operands must be valid numbers.
```

Expected exit code:

```text
1
```

### Checking Exit Codes

**PowerShell:**

```powershell
$LASTEXITCODE
```

**Bash/Zsh:**

```bash
echo $?
```

Exit codes are separate from printed application output.

---

## 9. Application Design

The application follows a simple processing pipeline:

```text
START
  |
  v
Receive CLI Arguments
  |
  v
Validate Argument Count
  |
  v
Validate Operands
  |
  v
Validate Operator
  |
  v
Perform Calculation
  |
  v
Display Result
  |
  v
Exit with Code 0
```

If validation or calculation fails:

```text
ERROR DETECTED
      |
      v
Display Error Message
      |
      v
Exit with Code 1
```

### Design Principles

**Deterministic behavior**

The same valid inputs should produce the same result.

**Separation of concerns**

Input handling, validation, calculation, and output should have clearly defined responsibilities.

**Shell independence**

Application logic should not depend on Bash, PowerShell, or another specific shell.

**Safe execution**

The calculator should implement supported operations explicitly rather than executing arbitrary user-supplied expressions using `eval()`.

**Testability**

Core calculation logic should be independently testable.

---

## 10. Testing Strategy

The project will use pytest for automated testing.

### Planned Test Cases

| Test ID | Input             | Expected Result |
| ------- | ----------------- | --------------- |
| TC-01   | `5 + 10`          | 15              |
| TC-02   | `10 - 5`          | 5               |
| TC-03   | `5 * 10`          | 50              |
| TC-04   | `10 / 2`          | 5               |
| TC-05   | `10 / 0`          | Error           |
| TC-06   | `hello + 10`      | Error           |
| TC-07   | `5 invalid 10`    | Error           |
| TC-08   | Missing arguments | Error           |
| TC-09   | Extra arguments   | Error           |
| TC-10   | `-5 + 10`         | 5               |
| TC-11   | `2.5 + 1.5`       | 4               |
| TC-12   | `5 - 4`           | 1               |

### Running Tests

Once pytest and the tests are installed:

```bash
python -m pytest
```

The testing strategy should verify both arithmetic correctness and CLI behavior, including exit codes and error messages.

---

## 11. Version Control

Git will be used throughout development.

### Initialize Repository

```bash
git init
```

### Check Repository Status

```bash
git status
```

### Stage Changes

```bash
git add .
```

### Commit Changes

```bash
git commit -m "Initialize Python CLI calculator project"
```

### Suggested Commit Milestones

| Milestone         | Commit Message                          |
| ----------------- | --------------------------------------- |
| Project setup     | `Initialize CLI calculator project`     |
| Argument handling | `Add command-line argument parsing`     |
| Validation        | `Implement input validation`            |
| Arithmetic        | `Implement calculator operations`       |
| Error handling    | `Add error handling and exit codes`     |
| Testing           | `Add automated calculator tests`        |
| Documentation     | `Update project documentation`          |
| Packaging         | `Configure Python package installation` |

---

## 12. Security Considerations

Although this is a beginner project, secure development principles should be followed.

### Security Requirements

* Do not execute arbitrary input using `eval()` or `exec()`.
* Validate all command-line arguments.
* Handle malformed input safely.
* Avoid unnecessary shell execution.
* Do not use `shell=True` for calculator operations.
* Do not expose sensitive system information in error messages.
* Keep project dependencies minimal.

These practices provide a foundation for more advanced security engineering.

---

## 13. Packaging and Distribution

A future project milestone is to package the application as an installable Python CLI.

The intended command will be:

```bash
calculator 5 + 10
```

Instead of:

```bash
python calculator.py 5 + 10
```

Packaging will introduce:

* Python project metadata
* `pyproject.toml`
* Console script entry points
* Local package installation
* Application distribution

Cloud hosting is not required for this calculator.

---

## 14. Development Roadmap

### Phase 1 — Foundation

* [ ] Create the project directory.
* [ ] Initialize Git.
* [ ] Create `calculator.py`.
* [ ] Implement command-line argument reading.

### Phase 2 — Validation

* [ ] Validate argument count.
* [ ] Validate numeric operands.
* [ ] Validate supported operators.
* [ ] Handle invalid input.

### Phase 3 — Calculator Logic

* [ ] Implement addition.
* [ ] Implement subtraction.
* [ ] Implement multiplication.
* [ ] Implement division.
* [ ] Handle division by zero.

### Phase 4 — Reliability

* [ ] Implement process exit codes.
* [ ] Write unit tests.
* [ ] Test CLI behavior.
* [ ] Refactor application code.

### Phase 5 — Release

* [ ] Complete documentation.
* [ ] Push the repository to GitHub.
* [ ] Configure packaging.
* [ ] Install and test the CLI locally.
* [ ] Create a versioned release.

---

## 15. Definition of Done

The project will be considered complete when:

* All four arithmetic operations work correctly.
* Invalid inputs are rejected safely.
* Errors produce appropriate non-zero exit codes.
* Successful calculations return exit code `0`.
* Automated tests pass.
* The application works in the intended supported environments.
* The code is tracked with Git.
* The README accurately describes the implemented application.
* The CLI can be installed and executed locally.

---

## 16. Learning Outcomes

After completing this project, the developer should be able to:

1. Explain how a shell launches a Python program.
2. Read command-line arguments using Python.
3. Validate user input.
4. Implement deterministic application logic.
5. Handle errors and process exit codes.
6. Write automated tests.
7. Manage source code with Git.
8. Document a software project.
9. Package a Python command-line application.
10. Apply basic secure coding principles.

---

## 17. Project Ownership

**Project:** Python CLI Calculator
**Training Program:** 60 Python Engineering Drills
**Organization:** JUGGERNAUT TECHNOLOGY SOLUTIONS
**Project Status:** In Development

---

**Powered by JUGGERNAUT TECHNOLOGY SOLUTIONS**

*Building software engineering capability through practical, project-based learning.*
