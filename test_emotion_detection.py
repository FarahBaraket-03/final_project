

from emotion_detection import detect_emotion

import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_detect_emotion(self):
        # Test case 1: Happy text
        result = detect_emotion("I am so happy today!")
        self.assertIn('joy', result)

        # Test case 2: Sad text
        result = detect_emotion("I feel very sad about this.")
        self.assertIn('sadness', result)

        # Test case 3: Angry text
        result = detect_emotion("This makes me really angry!")
        self.assertIn('anger', result)
        

if __name__ == '__main__':
    unittest.main()
