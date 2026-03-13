"""
Reading Rewards App - A Flask application to encourage children to read books.

This app presents a curated list of Grade-3-appropriate books, quizzes children
on their comprehension, and rewards them with coins that can be redeemed.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    """Home page showing coins, books completed, and next reward goal."""
    return "Home Page - Reading Rewards App"


@app.route('/books')
def books():
    """Display the library of available books."""
    return "Books Page - Browse Available Books"


@app.route('/quiz/<int:book_id>')
def quiz(book_id):
    """Display quiz questions for a specific book."""
    return f"Quiz Page - Book ID: {book_id}"


@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    """Handle quiz submission and evaluate answers."""
    return "Quiz Submitted"


@app.route('/rewards')
def rewards():
    """Display available rewards and redemption options."""
    return "Rewards Page - View and Redeem Rewards"


@app.route('/redeem_reward', methods=['POST'])
def redeem_reward():
    """Handle reward redemption."""
    return "Reward Redeemed"


@app.route('/progress')
def progress():
    """Display reading progress and achievements."""
    return "Progress Page - Your Reading Journey"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
