

from EmotionDetection.emotion_detection import emotion_detector

import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_detect_emotion(self):
        # Test case 1: Happy text
        result = emotion_detector("I am so happy today!")
        self.assertIn('joy', result)

        # Test case 2: Sad text
        result = emotion_detector("I feel very sad about this.")
        self.assertIn('sadness', result)

        # Test case 3: Angry text
        result = emotion_detector("This makes me really angry!")
        self.assertIn('anger', result)
        

if __name__ == '__main__':
    unittest.main()
