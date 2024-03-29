from unittest import TestCase
import dungeonsanddragons
import random


class TestGenerateSyllables(TestCase):
    def test_generate_syllables_length(self):
        self.assertEqual(len(dungeonsanddragons.generate_syllables()), 2)

    def test_generate_consonant_type(self):
        self.assertEqual(type(dungeonsanddragons.generate_syllables()), str)

    def test_generate_syllables_alpha(self):
        dnd_syllables = dungeonsanddragons.generate_syllables()
        self.assertTrue(dnd_syllables.isalpha())

    def test_generate_syllables_consonant(self):
        consonant_letters = 'bcdfghjklmnpqrstvwxyz'
        vowel_letters = 'aeiouy'
        syllable = dungeonsanddragons.generate_syllables()
        self.assertTrue(syllable[0] in consonant_letters and syllable[1] in vowel_letters)

    def test_generate_syllables_random(self):
        random.seed(4)
        fixed = dungeonsanddragons.generate_syllables()
        self.assertEqual("ki", fixed)
        random.seed()

