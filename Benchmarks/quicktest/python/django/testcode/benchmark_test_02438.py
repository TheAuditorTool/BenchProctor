# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import ipaddress
import socket
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02438(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    parsed = urlparse(data)
    resolved = socket.gethostbyname(parsed.hostname or data)
    if ipaddress.ip_address(resolved).is_private:
        return JsonResponse({'error': 'private range blocked'}, status=403)
    target_url = data.replace(parsed.hostname, resolved) if parsed.hostname else data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return JsonResponse({"saved": True})
