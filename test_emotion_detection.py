from Flask_EmotionDetection.emotion_detection import emotion_detector

import unittest
class TestEmotionDetection(unittest.TestCase):
    def test_emtion_detector(self):
        first = emotion_detector("I am glad this happened")
        self.assertEqual(first['dominant_emotion'],'joy')
        second = emotion_detector("I am really mad about this")
        self.assertEqual(second['dominant_emotion'],'anger')
        third = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(third['dominant_emotion'],'disgust')
        fourth = emotion_detector("I am so sad about this")
        self.assertEqual(fourth['dominant_emotion'],'sadness')
        fifth = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(fifth['dominant_emotion'],'fear')


unittest.main()