# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
from django.http import HttpResponse
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest75738(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse('<script src="' + str(processed) + '"></script>', content_type='text/html')
