#!/usr/bin/env python3

"""
# scrape.py

Scraping images and captions from <https://frinkiac.com>.

Licensed under "MIT No Attribution" (MIT-0), see LICENSE.
"""


EPISODE_COUNT_FROM_SEASON = {
  1: 13,
  2: 22,
  3: 24,
  4: 22,
  5: 22,
  6: 25,
  7: 25,
  8: 25,
  9: 25,
  10: 23,
  11: 22,
  12: 21,
  13: 22,
  14: 22,
  15: 22,
  16: 21,
  17: 22,
  18: 22,
  19: 20,
}


def construct_episode_url(season, episode):
  return f'https://frinkiac.com/episode/S{season:02}E{episode:02}/100000000'
