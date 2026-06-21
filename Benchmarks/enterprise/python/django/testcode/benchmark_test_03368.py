# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest03368(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
