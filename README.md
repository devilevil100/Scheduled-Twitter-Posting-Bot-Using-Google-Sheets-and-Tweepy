# Scheduled Twitter Posting Bot Using Google Sheets and Tweepy

This project is a Python-based Twitter bot that automates posting tweets based on scheduled times defined in a Google Sheet. It integrates Google Sheets API to read tweet content and schedule, and Tweepy library to post tweets on Twitter.

## Features
- Reads scheduled tweet data (date & time, tweet content, URL, hashtags, and post status) from a Google Sheets spreadsheet.
- Converts scheduled date and time from the sheet to UTC and compares it with the current time.
- Automatically posts tweets at the scheduled time if not already posted.
- Updates the posting status in the Google Sheet.
- Supports hashtags management by parsing comma-separated values.
- Runs continuously, checking every 10 seconds for due tweets.

## Prerequisites
- Python 3 environment
- Twitter Developer account with API keys and tokens
- Google Cloud project with Google Sheets API enabled and Service Account credentials JSON file

## Installation
1. Clone the repository:
