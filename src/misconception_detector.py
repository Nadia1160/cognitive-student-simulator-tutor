"""
Misconception Detector Module
=============================
Detects mathematical misconceptions in student responses.
"""

import re
from typing import Dict, Optional

class MisconceptionDetector:
    """Detects common mathematical misconceptions in student responses."""
    
    def __init__(self, patterns_path: Optional[str] = None):
        """
        Initialize the misconception detector.
        
        Args:
            patterns_path: Path to JSON file with misconception patterns
        """
        self.patterns = self._get_default_patterns()
        
        self.error_keywords = {
            "misconception_a": ['3x + 4', 'distribut', 'forgot to distribute'],
            "misconception_b": ['-5 - 3 = -2', 'sign error', 'negative'],
            "misconception_c": ['2/5', 'add numerators', 'add denominators']
        }
    
    def _get_default_patterns(self) -> Dict:
        """Get default misconception patterns."""
        return {
            "misconception_a": {
                "name": "Distributive Property Error",
                "description": "Student incorrectly distributes multiplication over addition",
                "example": "3(x+4) = 3x + 4"
            },
            "misconception_b": {
                "name": "Negative Sign Error",
                "description": "Student mishandles negative signs",
                "example": "-5 - 3 = -2"
            },
            "misconception_c": {
                "name": "Fraction Addition Error",
                "description": "Student adds numerators and denominators",
                "example": "1/2 + 1/3 = 2/5"
            }
        }
    
    def detect(self, response: str) -> Optional[Dict]:
        """
        Detect misconceptions in a student response.
        
        Args:
            response: Student's response text
            
        Returns:
            Dictionary with detected misconception or None
        """
        response_lower = response.lower()
        
        for pattern_id, keywords in self.error_keywords.items():
            for keyword in keywords:
                if keyword.lower() in response_lower:
                    return {
                        'misconception_id': pattern_id,
                        'name': self.patterns[pattern_id]['name'],
                        'confidence': 0.8,
                        'method': 'pattern_match'
                    }
        
        return None
