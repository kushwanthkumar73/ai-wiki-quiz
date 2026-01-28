# utils/quiz_generator.py

"""
TEMPORARY SAFE QUIZ GENERATOR
--------------------------------
This version avoids Gemini / LangChain issues.
Used only to verify FastAPI end-to-end flow.

Once API works, we will replace this with Gemini logic.
"""

def generate_quiz(text: str):
    """
    Generate quiz from Wikipedia article text.
    (Dummy implementation for now)
    """

    if not text or len(text.strip()) == 0:
        raise ValueError("Article text is empty")

    return {
        "quiz": [
            {
                "question": "Who is Alan Turing?",
                "options": [
                    "A British mathematician",
                    "A movie actor",
                    "A football player",
                    "A novelist"
                ],
                "answer": "A British mathematician",
                "difficulty": "easy",
                "explanation": "Alan Turing was a British mathematician and computer scientist."
            },
            {
                "question": "What is Alan Turing famous for?",
                "options": [
                    "Breaking the Enigma code",
                    "Inventing the telephone",
                    "Discovering gravity",
                    "Writing novels"
                ],
                "answer": "Breaking the Enigma code",
                "difficulty": "medium",
                "explanation": "He played a crucial role in breaking the Enigma code during World War II."
            }
        ],
        "related_topics": [
            "Enigma machine",
            "Cryptography",
            "Computer science history"
        ]
    }

