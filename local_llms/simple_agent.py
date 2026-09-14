#!/usr/bin/python

""" 
Trying to build an agent in python towards ollama locally.
Will try to build into other as well later
"""

# Libraries
import os
from datetime import datetime
from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider

# telling where to store notes to the agent
NOTES_FILE = 'notes.txt'

# Connect to local ai model
model = OllamaModel(
  '<name_of_model_used_on_local_server>',
  provider=OllamaProvider(base_url='<http://address_to_server:11434/v1>'),
)

# Methods
def get_curr_time() -> str:
  # "%Y, %B %d | %I:%M %p" = 2026, September 14 | 01:23 PM
  # "%Y, %m %d | %I:%M %p" = 2026, 09 14 | 01:23 PM
  # "%Y, %m %d | %H:%M" = 2026, 09 14 | 13:23 (better for logs/prigramming)
  '''Getting the current time and date '''
  return datetime.now().strftime('%Y, %B %d | %I:%M %p')

# this methods are linked to local store
def save_note(note: str) -> str:
  '''Store note for faster recall'''
  with open(NOTES_FILE, 'a', encoding='utf-8') as f:
    f.write(f'- {note}\n')
  return '[+] note stored...'

def read_note() -> str:
  '''Read stored notes from NOTES_FILE'''
  if not os.path.exists(NOTES_FILE): return '[-] no notes stored...'
  with opne(NOTES_FILE, encoding='utf-8') as f: return f.read()


