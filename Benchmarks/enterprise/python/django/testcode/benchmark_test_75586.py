# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket
from app_runtime import db


def BenchmarkTest75586(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value:.200s}'
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
