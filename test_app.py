"""
Tests for the Reading Rewards App Flask application.
"""

import json
import os
import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHomeRoute:
    """Tests for the home page route."""

    def test_home_returns_200(self, client):
        """Test that home page returns 200 status code."""
        response = client.get('/')
        assert response.status_code == 200

    def test_home_contains_expected_text(self, client):
        """Test that home page contains expected content."""
        response = client.get('/')
        assert b'Home Page' in response.data


class TestBooksRoute:
    """Tests for the books page route."""

    def test_books_returns_200(self, client):
        """Test that books page returns 200 status code."""
        response = client.get('/books')
        assert response.status_code == 200

    def test_books_contains_expected_text(self, client):
        """Test that books page contains expected content."""
        response = client.get('/books')
        assert b'Books Page' in response.data


class TestQuizRoute:
    """Tests for the quiz page route."""

    def test_quiz_returns_200(self, client):
        """Test that quiz page returns 200 status code."""
        response = client.get('/quiz/1')
        assert response.status_code == 200

    def test_quiz_contains_book_id(self, client):
        """Test that quiz page displays the book ID."""
        response = client.get('/quiz/42')
        assert b'Book ID: 42' in response.data

    def test_quiz_different_book_ids(self, client):
        """Test quiz page with different book IDs."""
        for book_id in [1, 5, 10, 50]:
            response = client.get(f'/quiz/{book_id}')
            assert response.status_code == 200
            assert f'Book ID: {book_id}'.encode() in response.data


class TestSubmitQuizRoute:
    """Tests for the quiz submission route."""

    def test_submit_quiz_post_returns_200(self, client):
        """Test that POST to submit_quiz returns 200 status code."""
        response = client.post('/submit_quiz')
        assert response.status_code == 200

    def test_submit_quiz_get_not_allowed(self, client):
        """Test that GET to submit_quiz is not allowed."""
        response = client.get('/submit_quiz')
        assert response.status_code == 405

    def test_submit_quiz_contains_expected_text(self, client):
        """Test that submit_quiz returns expected content."""
        response = client.post('/submit_quiz')
        assert b'Quiz Submitted' in response.data


class TestRewardsRoute:
    """Tests for the rewards page route."""

    def test_rewards_returns_200(self, client):
        """Test that rewards page returns 200 status code."""
        response = client.get('/rewards')
        assert response.status_code == 200

    def test_rewards_contains_expected_text(self, client):
        """Test that rewards page contains expected content."""
        response = client.get('/rewards')
        assert b'Rewards Page' in response.data


class TestRedeemRewardRoute:
    """Tests for the redeem reward route."""

    def test_redeem_reward_post_returns_200(self, client):
        """Test that POST to redeem_reward returns 200 status code."""
        response = client.post('/redeem_reward')
        assert response.status_code == 200

    def test_redeem_reward_get_not_allowed(self, client):
        """Test that GET to redeem_reward is not allowed."""
        response = client.get('/redeem_reward')
        assert response.status_code == 405

    def test_redeem_reward_contains_expected_text(self, client):
        """Test that redeem_reward returns expected content."""
        response = client.post('/redeem_reward')
        assert b'Reward Redeemed' in response.data


class TestProgressRoute:
    """Tests for the progress page route."""

    def test_progress_returns_200(self, client):
        """Test that progress page returns 200 status code."""
        response = client.get('/progress')
        assert response.status_code == 200

    def test_progress_contains_expected_text(self, client):
        """Test that progress page contains expected content."""
        response = client.get('/progress')
        assert b'Progress Page' in response.data


class TestBooksJson:
    """Tests for the books.json data file."""

    @pytest.fixture
    def books_data(self):
        """Load the books.json file."""
        books_path = os.path.join(os.path.dirname(__file__), 'books.json')
        with open(books_path, 'r') as f:
            return json.load(f)

    def test_books_json_exists(self):
        """Test that books.json file exists."""
        books_path = os.path.join(os.path.dirname(__file__), 'books.json')
        assert os.path.exists(books_path), "books.json file must exist"

    def test_books_json_is_valid_json(self):
        """Test that books.json contains valid JSON."""
        books_path = os.path.join(os.path.dirname(__file__), 'books.json')
        with open(books_path, 'r') as f:
            data = json.load(f)
        assert 'books' in data, "books.json must have a 'books' key"

    def test_books_count_is_50(self, books_data):
        """Test that there are exactly 50 books."""
        assert len(books_data['books']) == 50, "There must be exactly 50 books"

    def test_book_ids_are_sequential(self, books_data):
        """Test that book IDs are sequential from 1 to 50."""
        book_ids = [book['id'] for book in books_data['books']]
        expected_ids = list(range(1, 51))
        assert sorted(book_ids) == expected_ids, "Book IDs must be 1-50"

    def test_fiction_books_are_1_to_25(self, books_data):
        """Test that fiction books have IDs 1-25."""
        fiction_books = [b for b in books_data['books'] if b['category'] == 'fiction']
        fiction_ids = [b['id'] for b in fiction_books]
        assert sorted(fiction_ids) == list(range(1, 26)), "Fiction books must have IDs 1-25"

    def test_nonfiction_books_are_26_to_50(self, books_data):
        """Test that nonfiction books have IDs 26-50."""
        nonfiction_books = [b for b in books_data['books'] if b['category'] == 'nonfiction']
        nonfiction_ids = [b['id'] for b in nonfiction_books]
        assert sorted(nonfiction_ids) == list(range(26, 51)), "Nonfiction books must have IDs 26-50"

    def test_all_books_have_required_fields(self, books_data):
        """Test that all books have required fields."""
        required_fields = ['id', 'title', 'author', 'category', 'description', 'coins', 'questions']
        for book in books_data['books']:
            for field in required_fields:
                assert field in book, f"Book {book.get('id', 'unknown')} missing field: {field}"

    def test_book_categories_are_valid(self, books_data):
        """Test that all book categories are either 'fiction' or 'nonfiction'."""
        valid_categories = {'fiction', 'nonfiction'}
        for book in books_data['books']:
            assert book['category'] in valid_categories, \
                f"Book {book['id']} has invalid category: {book['category']}"

    def test_coin_values_are_in_range(self, books_data):
        """Test that coin values are between 5 and 15."""
        for book in books_data['books']:
            assert 5 <= book['coins'] <= 15, \
                f"Book {book['id']} has coins {book['coins']} outside range 5-15"

    def test_each_book_has_3_to_5_questions(self, books_data):
        """Test that each book has 3-5 questions."""
        for book in books_data['books']:
            num_questions = len(book['questions'])
            assert 3 <= num_questions <= 5, \
                f"Book {book['id']} has {num_questions} questions, expected 3-5"

    def test_questions_have_required_fields(self, books_data):
        """Test that all questions have required fields."""
        required_fields = ['question', 'options', 'answer']
        for book in books_data['books']:
            for i, question in enumerate(book['questions']):
                for field in required_fields:
                    assert field in question, \
                        f"Book {book['id']} question {i+1} missing field: {field}"

    def test_questions_have_4_options(self, books_data):
        """Test that each question has exactly 4 options."""
        for book in books_data['books']:
            for i, question in enumerate(book['questions']):
                assert len(question['options']) == 4, \
                    f"Book {book['id']} question {i+1} has {len(question['options'])} options, expected 4"

    def test_answer_is_one_of_options(self, books_data):
        """Test that the answer is one of the available options."""
        for book in books_data['books']:
            for i, question in enumerate(book['questions']):
                assert question['answer'] in question['options'], \
                    f"Book {book['id']} question {i+1} answer '{question['answer']}' not in options"

    def test_book_titles_are_not_empty(self, books_data):
        """Test that all book titles are non-empty strings."""
        for book in books_data['books']:
            assert isinstance(book['title'], str) and len(book['title']) > 0, \
                f"Book {book['id']} has invalid title"

    def test_book_authors_are_not_empty(self, books_data):
        """Test that all book authors are non-empty strings."""
        for book in books_data['books']:
            assert isinstance(book['author'], str) and len(book['author']) > 0, \
                f"Book {book['id']} has invalid author"

    def test_book_descriptions_are_not_empty(self, books_data):
        """Test that all book descriptions are non-empty strings."""
        for book in books_data['books']:
            assert isinstance(book['description'], str) and len(book['description']) > 0, \
                f"Book {book['id']} has invalid description"

    def test_question_texts_are_not_empty(self, books_data):
        """Test that all question texts are non-empty strings."""
        for book in books_data['books']:
            for i, question in enumerate(book['questions']):
                assert isinstance(question['question'], str) and len(question['question']) > 0, \
                    f"Book {book['id']} question {i+1} has invalid question text"

    def test_options_are_not_empty(self, books_data):
        """Test that all options are non-empty strings."""
        for book in books_data['books']:
            for i, question in enumerate(book['questions']):
                for j, option in enumerate(question['options']):
                    assert isinstance(option, str) and len(option) > 0, \
                        f"Book {book['id']} question {i+1} option {j+1} is invalid"

    def test_specific_fiction_books_present(self, books_data):
        """Test that specific fiction books from requirements are present."""
        expected_titles = [
            "Charlotte's Web",
            "Because of Winn-Dixie",
            "The Tale of Despereaux",
            "Ramona Quimby, Age 8",
            "Pippi Longstocking",
            "James and the Giant Peach",
            "The BFG",
            "Fantastic Mr. Fox",
            "The Boxcar Children",
            "My Father's Dragon"
        ]
        book_titles = [b['title'] for b in books_data['books']]
        for title in expected_titles:
            assert title in book_titles, f"Expected fiction book '{title}' not found"

    def test_specific_nonfiction_books_present(self, books_data):
        """Test that specific nonfiction books from requirements are present."""
        expected_titles = [
            "Who Was Albert Einstein?",
            "Who Was Amelia Earhart?",
            "Who Was Neil Armstrong?",
            "Who Was Martin Luther King Jr.?",
            "Who Was Rosa Parks?",
            "Who Was Steve Jobs?"
        ]
        book_titles = [b['title'] for b in books_data['books']]
        for title in expected_titles:
            assert title in book_titles, f"Expected nonfiction book '{title}' not found"
