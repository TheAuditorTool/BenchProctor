# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse
import unicodedata


def BenchmarkTest22713(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', cookie_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = cookie_value
    normalized = unicodedata.normalize('NFKC', str(processed))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
