"""
Tests for the Reading Rewards App Flask application.
"""

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
