"""
Tests for the Cognitive Student Simulator Tutor project.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.student_simulator import StudentSimulator
from src.misconception_detector import MisconceptionDetector
from src.tutor_agent import TutorAgent

class TestStudentSimulator:
    """Test cases for StudentSimulator class."""
    
    def setup_method(self):
        """Setup before each test."""
        self.simulator = StudentSimulator()
    
    def test_profile_loading(self):
        """Test that profiles load correctly."""
        assert len(self.simulator.profiles) == 3
        assert 'low_achiever' in self.simulator.profiles
        assert 'medium_achiever' in self.simulator.profiles
        assert 'high_achiever' in self.simulator.profiles
    
    def test_response_generation(self):
        """Test that responses are generated."""
        response = self.simulator.generate_response('low_achiever', 'Solve for x: 3(x+4)=21')
        assert response is not None
        assert isinstance(response, str)

class TestMisconceptionDetector:
    """Test cases for MisconceptionDetector class."""
    
    def setup_method(self):
        """Setup before each test."""
        self.detector = MisconceptionDetector()
    
    def test_pattern_detection(self):
        """Test that misconceptions are detected."""
        # Test distributive property error
        result = self.detector.detect("3(x+4) = 3x + 4")
        assert result is not None
        assert result['misconception_id'] == 'misconception_a'
        
        # Test negative sign error
        result = self.detector.detect("-5 - 3 = -2")
        assert result is not None
        assert result['misconception_id'] == 'misconception_b'
        
        # Test fraction addition error
        result = self.detector.detect("1/2 + 1/3 = 2/5")
        assert result is not None
        assert result['misconception_id'] == 'misconception_c'

class TestTutorAgent:
    """Test cases for TutorAgent class."""
    
    def setup_method(self):
        """Setup before each test."""
        self.detector = MisconceptionDetector()
        self.tutor = TutorAgent(self.detector)
    
    def test_tutor_session_with_error(self):
        """Test tutor session when error is detected."""
        result = self.tutor.tutor_session(
            "Solve for x: 3(x+4)=21",
            "3(x+4) = 3x + 4, so x = 17/3"
        )
        assert result['diagnosis'] is not None
        assert 'feedback' in result
    
    def test_tutor_session_without_error(self):
        """Test tutor session when no error is detected."""
        result = self.tutor.tutor_session(
            "Solve for x: 3(x+4)=21",
            "3(x+4) = 3x + 12, so x = 3"
        )
        assert result['diagnosis'] is None
        assert 'feedback' in result

if __name__ == '__main__':
    pytest.main(['-v', __file__])
