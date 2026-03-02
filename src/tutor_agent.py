"""
Tutor Agent Module
==================
Provides intelligent, error-aware tutoring feedback.
"""

from typing import Dict, Optional, List
from datetime import datetime
import random

class TutorAgent:
    """Intelligent tutor agent that provides error-aware feedback."""
    
    def __init__(self, detector):
        """
        Initialize the tutor agent.
        
        Args:
            detector: MisconceptionDetector instance
        """
        self.detector = detector
        self.conversation_history = []
        
        self.feedback_templates = {
            "misconception_a": (
                "I notice you might have trouble with the distributive property. "
                "Remember: a(b + c) = ab + ac. Try multiplying the outside term "
                "by EVERY term inside the parentheses."
            ),
            "misconception_b": (
                "Be careful with negative numbers. On a number line, -5 - 3 means "
                "starting at -5 and moving LEFT 3 spaces to -8."
            ),
            "misconception_c": (
                "When adding fractions, you need a common denominator first. "
                "You can't just add numerators and denominators."
            )
        }
        
        self.encouragements = [
            "Good attempt! Let's work through this together.",
            "I see where you're coming from. Here's another way to think about it.",
            "You're on the right track! Let me help you refine your approach.",
            "Great effort! Let's break this down step by step."
        ]
    
    def tutor_session(self, question: str, response: str, 
                     student_id: Optional[str] = None) -> Dict:
        """
        Run a tutoring session.
        
        Args:
            question: The math question
            response: Student's response
            student_id: Optional student identifier
            
        Returns:
            Dictionary with diagnosis and feedback
        """
        diagnosis = self.detector.detect(response)
        
        if diagnosis:
            feedback = self.feedback_templates.get(
                diagnosis['misconception_id'],
                "Let's review this concept together."
            )
        else:
            encouragement = random.choice(self.encouragements)
            feedback = f"{encouragement} Can you explain your reasoning step by step?"
        
        self.conversation_history.append({
            'timestamp': str(datetime.now()),
            'student_id': student_id,
            'question': question,
            'response': response,
            'diagnosis': diagnosis['name'] if diagnosis else None,
            'feedback': feedback
        })
        
        return {
            'diagnosis': diagnosis,
            'feedback': feedback
        }
    
    def get_history(self) -> List[Dict]:
        """Get conversation history."""
        return self.conversation_history
