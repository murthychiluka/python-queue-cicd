# Python Queue Data Structure with CI/CD

## 1. Project Overview

This project demonstrates the implementation of a **Queue Data Structure using Python** and automates unit testing using **GitHub Actions CI/CD**.

A Queue follows the FIFO (First In, First Out) principle.

FIFO means the element inserted first will be removed first.

### Real-world example

Consider people standing in a ticket booking queue.

- The person who enters first gets served first.
- New people join at the rear.
- People leave from the front.

## 2. Project Objectives

- Understand Queue Data Structure.
- Implement Queue operations using Python classes and objects.
- Understand FIFO (First In, First Out).
- Write automated unit tests using Python `unittest`.
- Integrate automated testing with GitHub Actions.
- Understand basic CI/CD workflow.

## 3. Queue Operations

| Operation | Description |
|---|---|
| `enqueue()` | Adds an element to the rear of the queue |
| `dequeue()` | Removes an element from the front |
| `display()` | Displays all queue elements |

### Example

Initial Queue:

`[]`

After enqueue operations:

```python
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
```

Queue:

`[10, 20, 30]`

After dequeue:

```python
q.dequeue()
```

Updated Queue:

`[20, 30]`

The element `10` is removed because it entered first.

## 4. Project Folder Structure

```text
python-queue-cicd/
│
├── my_queue.py
├── test_queue.py
├── requirements.txt
│
└── .github/
    └── workflows/
        └── main.yml
```

## 5. Technologies Used

- Python 3.11 / 3.12
- Python Classes and Objects
- List Data Structure
- Python unittest Framework
- Git and GitHub
- GitHub Actions

## 6. Unit Testing

Python's built-in `unittest` framework is used to validate Queue operations.

### Test cases

1. `test_enqueue` – Validates insertion of elements.
2. `test_dequeue` – Validates removal of the first element.
3. `test_empty_queue` – Validates behaviour when removing an element from an empty queue.

### Execute unit tests locally

```bash
python -m unittest -v test_queue.py
```

### Expected result

```text
test_dequeue ... ok
test_empty_queue ... ok
test_enqueue ... ok

Ran 3 tests

OK
```

## 7. CI/CD Pipeline – GitHub Actions

GitHub Actions automates the testing process whenever code is pushed to the `main` branch or a pull request targets `main`.

### Pipeline workflow

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions Trigger
    |
    v
Checkout Source Code
    |
    v
Setup Python Environment
    |
    v
Install Dependencies
    |
    v
Execute Python Application
    |
    v
Run Unit Tests
    |
    v
Pipeline Success / Failure
```

### GitHub Actions responsibilities

| Step | Description |
|---|---|
| Checkout | Downloads repository source code |
| Setup Python | Configures Python runtime |
| Install dependencies | Installs required packages |
| Run application | Executes Python Queue application |
| Run tests | Executes automated unit tests |

## 8. Git Commands

Initialize Git repository:

```bash
git init
```

Add files:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Initial Python Queue application"
```

Push to GitHub:

```bash
git push -u origin main
```

For future code changes:

```bash
git add .
git commit -m "Updated queue implementation"
git push
```

## 9. Key Learning Outcomes

- Understanding FIFO data structure.
- Implementing Queue using Python lists.
- Understanding constructors (`__init__`).
- Understanding instance variables (`self.queue`).
- Understanding methods and objects.
- Writing automated unit tests.
- Understanding Python module imports.
- Understanding CI/CD automation.
- Integrating Python applications with GitHub Actions.

## 10. Future Enhancements

- Implement Stack Data Structure.
- Implement Linked List.
- Implement Circular Queue.
- Add more unit test cases.
- Generate test coverage reports.
- Build a Docker image.
- Push Docker image to Docker Hub or AWS ECR.
- Deploy the application to Kubernetes (Amazon EKS).

## 11. Project Summary

This hands-on project demonstrates how a basic Python Data Structure application can be integrated with a CI/CD pipeline.

It connects Python programming fundamentals with practical DevOps automation using GitHub Actions.
