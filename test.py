import unittest
from hasher import Hasher
from collections import defaultdict


class TestHash(unittest.TestCase):
    def setUp(self):
        self.hasher = Hasher("words.txt", nwords=3, delimeter="-")

    def test_smoke_test(self):
        data = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi"""
        self.assertEqual(self.hasher.process(
            data), "Isaac-Bremely-Trueheartedly")

    def test_long_text(self):
        data = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. In non egestas dolor. Nulla molestie sed justo sed elementum. Aliquam erat volutpat. Morbi odio lectus, consequat nec nisl eu, vulputate convallis ex. Etiam faucibus lorem non tempus malesuada. Praesent aliquet, ligula et fringilla euismod, nulla felis accumsan est, bibendum semper ligula ligula ut leo. Donec nibh metus, fermentum in fermentum id, vulputate vel sapien. Quisque gravida eros in rhoncus convallis.
Proin eu dui finibus, maximus nisl sed, dignissim odio. Fusce vel est eu justo imperdiet suscipit eu mattis turpis. Nam sed odio sollicitudin, pulvinar purus non, mollis nulla. Nam sed euismod orci, sed vestibulum mauris. Curabitur cursus est in ornare mollis. Nulla urna turpis, tincidunt non tempor eu, auctor et nisi. Vivamus lobortis elit vel dolor pharetra blandit. Morbi in feugiat odio.
In nec augue velit. Suspendisse interdum purus in metus luctus, eu rhoncus mauris porta. Aliquam pharetra, elit vitae convallis congue, libero velit malesuada felis, sed sodales turpis enim sed leo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam auctor tortor ut semper pretium. Aenean sed malesuada nisi, eget venenatis enim. Suspendisse in sagittis arcu, eu tristique turpis. Mauris dignissim eget ex sit amet egestas. Donec blandit dolor quis sapien aliquet, id rutrum lorem ultrices. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
Ut id scelerisque sem. Cras bibendum, lorem vel dapibus placerat, odio mauris finibus sapien, a efficitur purus massa et metus. Vestibulum dolor elit, ultrices quis enim in, convallis sagittis metus. Phasellus lacinia justo elit, non elementum augue pellentesque eu. Sed nec eleifend enim. Quisque blandit felis quis porta sodales. Morbi id rutrum tellus. Integer varius felis non luctus placerat. Praesent a lacus est. Nulla sollicitudin volutpat erat, pulvinar sagittis dui imperdiet sed. Nulla tempor, leo vel malesuada ullamcorper, libero eros rutrum sem, non ullamcorper tortor ex sed nibh. Cras ac lectus vitae elit dignissim rutrum. Etiam non semper mauris. Donec sem velit, elementum sit amet nibh a, pellentesque maximus velit. Nam ac velit ligula.
"""

        self.assertEqual(self.hasher.process(
            data), "Blips-Laggingly-Trochilidae")

    def test_short_text(self):
        data = """s"""
        self.assertEqual(self.hasher.process(data), "Abaca-Abusage-Blisses")

    def test_non_text_data(self):
        data = {"hello": 1, "other": "lorem"}
        self.assertEqual(self.hasher.process(
            data), "Interindividual-Fastbacks-Allochetite")

    def test_hash_distribution(self):
        results = defaultdict(list)
        collisions = 0
        with open("words.txt") as input:
            for line in input:
                hashed = self.hasher.process(line)
                if hashed in results:
                    collisions += 1
                results[hashed].append(line)

        print("Collided:")
        print({k: v for k, v in results.items() if len(v) > 1})

        # words has 370102 unique words, expect very few collisions
        self.assertLessEqual(collisions, 5)


if __name__ == '__main__':
    unittest.main()
