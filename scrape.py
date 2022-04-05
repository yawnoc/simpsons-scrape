#!/usr/bin/env python3

"""
# scrape.py

Scrape time ranges, image URLs, and captions from <https://frinkiac.com>,
dumping unto CSV files in the `output/` directory.

Licensed under "MIT No Attribution" (MIT-0), see LICENSE.
"""


import csv
import os
import re
import requests_html
import time


DOMAIN = 'https://frinkiac.com'
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


def extract_image_id(small_image_url):
  
  if small_image_url is None:
    return None
  
  match = re.match(r'/img/.+/(?P<image_id>.+?)/small\.jpg', small_image_url)
  
  try:
    return match.group('image_id')
  except AttributeError:
    return None


def construct_large_image_full_url(season, episode, image_id):
  return f'https://frinkiac.com/img/S{season:02}E{episode:02}/{image_id}/large.jpg'


def construct_output_file_name(season, episode):
  return f'output/S{season:02}E{episode:02}.csv'


def scrape_data(season, episode):
  
  output_file_name = construct_output_file_name(season, episode)
  if os.path.exists(output_file_name): # assume complete
    return
  
  season_episode_string = f'S{season:02}E{episode:02}'
  start_time = time.perf_counter()
  print(f'Started scrape for {season_episode_string}')
  
  session = requests_html.HTMLSession()
  response = session.get(construct_episode_url(season, episode))
  if not response:
    print(f'Got {response} for {season_episode_string}')
    return
  
  with open(output_file_name, 'w', encoding='utf-8', newline='') as csv_file:
    
    csv_writer = csv.writer(csv_file)
    
    response.html.render()
    for n, row in enumerate(response.html.find('div.episode-subtitle.row')):
      
      try:
        time_range = row.find('small', first=True).text
      except AttributeError:
        print(f'No time range found for row {n} of {season_episode_string}')
        time_range = None
      
      try:
        small_image_url = row.find('img', first=True).attrs['src']
      except (AttributeError, KeyError):
        print(f'No image found for row {n} of {season_episode_string}')
        small_image_url = None
      
      image_id = extract_image_id(small_image_url)
      large_image_full_url = \
              construct_large_image_full_url(season, episode, image_id)
      
      try:
        caption = row.find('p', first=True).text
      except AttributeError:
        print(f'No caption found for row {n} of {season_episode_string}')
        caption = None
      
      csv_writer.writerow([time_range, large_image_full_url, caption])
    
    finish_time = time.perf_counter()
    duration_string = f'{finish_time - start_time:0.1f}s'
    print(f'Finished scrape for {season_episode_string} in {duration_string}')


def main():
  for season, episode_count in EPISODE_COUNT_FROM_SEASON.items():
    for episode in range(1, episode_count+1):
      scrape_data(season, episode)


if __name__ == '__main__':
  main()
