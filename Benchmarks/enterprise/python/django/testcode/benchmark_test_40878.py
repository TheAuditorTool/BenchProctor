# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest40878(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = normalise_input(comment_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
