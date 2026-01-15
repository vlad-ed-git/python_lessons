"""
Simple API Server using only Python standard library
Serves data from an in-memory array
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs
