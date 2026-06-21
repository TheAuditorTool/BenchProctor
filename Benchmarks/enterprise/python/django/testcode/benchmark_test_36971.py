# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import re
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest36971(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = default_blank(comment_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    return redirect(str(data))
