#!/usr/bin/env python3

"""
# test_scrape.py

Perform unit testing for `scrape.py`.

Licensed under "MIT No Attribution" (MIT-0), see LICENSE.
"""


import scrape
import unittest


class TestCmd(unittest.TestCase):
  
  def test_construct_episode_url(self):
    self.assertEqual(
      scrape.construct_episode_url(3, 4),
      'https://frinkiac.com/episode/S03E04/100000000'
    )
    self.assertEqual(
      scrape.construct_episode_url(8, 25),
      'https://frinkiac.com/episode/S08E25/100000000'
    )
    self.assertEqual(
      scrape.construct_episode_url(16, 1),
      'https://frinkiac.com/episode/S16E01/100000000'
    )
    self.assertEqual(
      scrape.construct_episode_url(19, 20),
      'https://frinkiac.com/episode/S19E20/100000000'
    )


if __name__ == '__main__':
  unittest.main()
