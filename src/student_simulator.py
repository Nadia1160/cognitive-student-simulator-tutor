"""
Student Simulator Module
=======================
Simulates student responses based on cognitive profiles and misconceptions.
"""

import random
import json
from typing import Dict, List, Optional

class StudentSimulator:
    """Simulates student responses with different learning profiles."""
    
    def __init__(self, profiles_path: Optional[str] = None):
        """
        Initialize the student simulator.
        
        Args:
            profiles_path: Path to JSON file with student profiles
        """
        if profiles_path:
            with open(profiles_path, 'r') as f:
                self.profiles = json.load(f)
        else:
            self.profiles = self._get_default_profiles()
    
    def _get_default_profiles(self) -> Dict:
        """Get default student profiles."""
        return {
            "low_achiever": {
                "name": "Alex",
                "grade_level": 8,
                "math_ability": 0.3,
                "confidence": 0.4,
                "description": "Struggles with basic concepts"
            },
            "medium_achiever": {
                "name": "Jamal",
                "grade_level": 9,
                "math_ability": 0.6,
                "confidence": 0.7,
                "description": "Understands concepts but makes procedural errors"
            },
            "high_achiever": {
                "name": "Maria",
                "grade_level": 10,
                "math_ability": 0.9,
                "confidence": 0.9,
                "description": "Methodical and confident problem solver"
            }
        }
    
    def generate_response(self, profile_id: str, question: str) -> str:
        """
        Generate a simulated student response.
        
        Args:
            profile_id: ID of student profile to use
            question: Math question to respond to
            
        Returns:
            Simulated student response
        """
        if profile_id == 'low_achiever':
            responses = [
                "I think the answer is 42? I'm not sure.",
                f"Can you help me? I don't understand {question[:20]}...",
                "3(x+4) = 3x + 4, so x = 17/3",
                "-5 - 3 = -2 because subtracting makes it smaller",
                "1/2 + 1/3 = 2/5"
            ]
        elif profile_id == 'medium_achiever':
            responses = [
                "Let me think step by step...",
                "I need to find a common denominator first.",
                "3(x+4) = 3x + 12, so 3x = 9, x = 3",
                "-5 - 3 = -8, is that right?",
                "1/2 + 1/3 = 3/6 + 2/6 = 5/6"
            ]
        else:  # high_achiever
            responses = [
                "This is straightforward. Let me solve it systematically.",
                "3(x+4) = 21 → 3x + 12 = 21 → 3x = 9 → x = 3",
                "-5 - 3 = -8 (moving left on number line)",
                "1/2 + 1/3 = 3/6 + 2/6 = 5/6"
            ]
        
        return random.choice(responses)
    
    def get_profile_info(self, profile_id: str) -> Dict:
        """Get information about a specific profile."""
        return self.profiles.get(profile_id, {})
