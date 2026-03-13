# Requirements

## Overview

Build a **simple local web application** that encourages a Grade 3 child to read fiction and non-fiction books and track their progress.

The app presents a curated list of **50 Grade-3-appropriate books**. When the child claims they have read a book, the app asks a few comprehension questions. If the child answers most of them correctly, the book is marked as completed and the child earns **reward coins**.

Coins can be redeemed for small real-world rewards such as ice cream, chocolate, or a movie night.

The application must run **locally on a Mac** with minimal setup and no external services.

The system will be implemented with **Python and Flask** and should be easy for a parent to run locally.

---

# Goals

The system must:

1. Encourage consistent reading.
2. Track books completed by the child.
3. Verify reading comprehension through simple quizzes.
4. Reward reading with coins.
5. Allow coins to be redeemed for rewards.
6. Keep the application extremely simple to run locally.

---

# Functional Requirements

## 1. Home Screen

The home page must display:

* Child name (configurable)
* Total coins earned
* Books completed
* Remaining books
* Next reward goal

Example display:

```
Coins: 45
Books Completed: 7
Next Reward: Ice Cream (50 coins)
```

---

# 2. Book Library

The app must include **50 preloaded books** suitable for Grade-3 readers.

Each book must include:

* id
* title
* author
* category (fiction / nonfiction)
* description
* coin reward value
* quiz questions

Example structure:

```
{
  "id": 1,
  "title": "Charlotte's Web",
  "author": "E.B. White",
  "category": "fiction",
  "coins": 10
}
```

Each book must contain **3–5 multiple-choice quiz questions**.

---

# 3. Mark Book as Read

Each book must have a button:

```
I Read This Book
```

When clicked:

1. The quiz page opens.
2. The child answers 3–5 questions.

Example:

```
Who is Wilbur?

A pig
A dog
A horse
A spider
```

---

# 4. Quiz Evaluation

Rules:

* If **≥70% of questions are correct**, the book is marked completed.
* The child receives the book's coin reward.

Success message example:

```
Great Job!
You earned 10 coins.
```

Failure example:

```
Nice try!
Read the book again and try later.
```

Books cannot be completed more than once.

---

# 5. Rewards System

Coins accumulate from completed books.

Rewards available:

| Reward      | Coins Required |
| ----------- | -------------- |
| Chocolate   | 30             |
| Ice Cream   | 50             |
| Movie Night | 120            |

When the child has enough coins, the reward page must allow redemption.

Redeeming a reward must:

* subtract coins
* record the redeemed reward

---

# 6. Progress Dashboard

The progress page must show:

* total coins earned
* books completed
* list of completed books
* rewards redeemed

---

# 7. Local Persistence

All data must be stored locally.

Required storage files:

```
books.json
user_progress.json
```

Example `user_progress.json`:

```
{
  "coins": 20,
  "books_completed": ["Charlotte's Web"],
  "rewards_redeemed": []
}
```

Data must persist between app runs.

---

# Technical Requirements

## Backend

Language:

Python

Framework:

Flask

No databases required.

---

## Frontend

Simple stack only:

* HTML
* CSS
* minimal JavaScript

Do NOT use:

* React
* Vue
* Angular

---

# Project Structure

The application must follow this exact directory structure:

```
reading-rewards-app/

app.py
books.json
user_progress.json
requirements.txt

/templates
    base.html
    home.html
    books.html
    quiz.html
    rewards.html
    progress.html

/static
    style.css
```

---

# File Responsibilities

## app.py

Main Flask server.

Responsibilities:

* start web server
* load books data
* load user progress
* render pages
* handle quiz submission
* update progress
* award coins
* manage rewards

Required routes:

```
/
/books
/quiz/<book_id>
/submit_quiz
/rewards
/redeem_reward
/progress
```

---

## books.json

Contains the **50 books and quiz questions**.

Example format:

```
{
  "books": [
    {
      "id": 1,
      "title": "Charlotte's Web",
      "author": "E.B. White",
      "category": "fiction",
      "coins": 10,
      "questions": [
        {
          "question": "Who is Wilbur?",
          "options": ["A pig","A horse","A dog","A spider"],
          "answer": "A pig"
        }
      ]
    }
  ]
}
```

Each book must include:

* 3–5 quiz questions.

---

## user_progress.json

Stores reading progress.

Example:

```
{
  "coins": 0,
  "books_completed": [],
  "rewards_redeemed": []
}
```

---

## requirements.txt

Must include:

```
Flask
```

---

# UI Requirements

The UI must be **kid-friendly**.

Guidelines:

* large fonts
* big buttons
* simple layout
* bright colors
* minimal text

Navigation bar must contain:

```
Home | Books | Rewards | Progress
```

---

# Pages

## Home

Shows:

* coins earned
* books completed
* next reward goal

---

## Books

Displays:

* book title
* author
* category
* "I Read This Book" button

---

## Quiz

Displays questions and multiple-choice answers.

Shows pass/fail result.

---

## Rewards

Shows available rewards and redemption buttons.

---

## Progress

Shows:

* completed books
* rewards redeemed
* coin history

---

# Book List (50 Books)

## Fiction

1. Charlotte's Web — E.B. White
2. Because of Winn-Dixie — Kate DiCamillo
3. The Tale of Despereaux — Kate DiCamillo
4. Ramona Quimby, Age 8 — Beverly Cleary
5. Pippi Longstocking — Astrid Lindgren
6. James and the Giant Peach — Roald Dahl
7. The BFG — Roald Dahl
8. Fantastic Mr. Fox — Roald Dahl
9. The Boxcar Children — Gertrude Chandler Warner
10. My Father's Dragon — Ruth Stiles Gannett
11. The Mouse and the Motorcycle — Beverly Cleary
12. Frindle — Andrew Clements
13. The Wild Robot — Peter Brown
14. Mr. Popper's Penguins — Richard Atwater
15. The Chocolate Touch — Patrick Skene Catling
16. Magic Tree House: Dinosaurs Before Dark — Mary Pope Osborne
17. Magic Tree House: The Knight at Dawn — Mary Pope Osborne
18. Stuart Little — E.B. White
19. Matilda — Roald Dahl
20. The Borrowers — Mary Norton
21. Sideways Stories from Wayside School — Louis Sachar
22. The Hundred Dresses — Eleanor Estes
23. Sarah, Plain and Tall — Patricia MacLachlan
24. The Miraculous Journey of Edward Tulane — Kate DiCamillo
25. The Secret Garden (adapted)

---

## Non-Fiction

26. Who Was Albert Einstein?
27. Who Was Amelia Earhart?
28. Who Was Neil Armstrong?
29. Who Was Martin Luther King Jr.?
30. Who Was Rosa Parks?
31. Who Was Steve Jobs?
32. National Geographic Kids: Weird But True
33. National Geographic Kids: Sharks
34. National Geographic Kids: Space Encyclopedia
35. DK Children's Encyclopedia
36. The Magic School Bus Inside the Human Body
37. The Magic School Bus Lost in the Solar System
38. Who Would Win? T-Rex vs Velociraptor
39. I Am Jane Goodall
40. I Am Helen Keller
41. I Am Walt Disney
42. The Boy Who Harnessed the Wind (Young Readers Edition)
43. National Geographic Kids: Volcanoes
44. National Geographic Kids: Weather
45. DK Find Out! Animals
46. DK Find Out! Space
47. DK Find Out! Dinosaurs
48. What If You Had Animal Teeth?
49. What If You Had Animal Hair?
50. What If You Had Animal Eyes?

---

# Setup Instructions

Parent setup must be simple:

```
git clone <repo>
cd reading-rewards-app
pip install -r requirements.txt
python app.py
```

Open browser:

```
http://localhost:5000
```

---

# Out of Scope

Not required for this version:

* login systems
* databases
* cloud sync
* mobile apps
* library APIs
* payments
* multiple users

---

# Notes

Key design principle:

```
Keep the application extremely simple, local, and easy for parents to run.
```

Possible future enhancements:

* multiple children profiles
* reading streaks
* more books
* AI-generated quizzes
* difficulty progression
