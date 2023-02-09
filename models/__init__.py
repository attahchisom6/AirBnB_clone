#!/usr/bin/python3
"""to create a unique file storave instance for my appllication"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
