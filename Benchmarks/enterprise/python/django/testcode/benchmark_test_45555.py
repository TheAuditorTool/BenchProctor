# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import re
import ast


def BenchmarkTest45555(request):
    user_id = request.GET.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    digest = hashlib.md5(str(processed).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
