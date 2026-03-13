# Reading Rewards App

A simple local web application that encourages Grade 3 children to read fiction and non-fiction books and track their progress.

## Design Overview

The app presents a curated list of 50 Grade-3-appropriate books. When a child claims they have read a book, the app asks comprehension questions. If the child answers most correctly (70% or more), the book is marked as completed and the child earns reward coins.

Coins can be redeemed for small real-world rewards such as ice cream, chocolate, or a movie night.

### Features

- **Home Dashboard**: Shows coins earned, books completed, and next reward goal
- **Book Library**: Browse 50 curated books suitable for Grade 3 readers
- **Quiz System**: Answer comprehension questions to prove you read the book
- **Rewards**: Redeem earned coins for real-world rewards
- **Progress Tracking**: View completed books and redeemed rewards

### Technical Stack

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, minimal JavaScript
- **Storage**: Local JSON files (no database required)

## Installation Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd reading-rewards-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## How to Run Tests

Run the test suite using pytest:

```bash
pytest
```

For verbose output:

```bash
pytest -v
```

## Project Structure

```
reading-rewards-app/
├── app.py                 # Main Flask server
├── books.json             # Book library with quiz questions
├── user_progress.json     # User progress data
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── templates/             # HTML templates
└── static/                # CSS and static assets
```
