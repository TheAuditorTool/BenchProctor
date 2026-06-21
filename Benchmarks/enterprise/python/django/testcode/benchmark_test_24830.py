# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse
import json
import unicodedata


def to_text(value):
    return str(value).strip()

def BenchmarkTest24830(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
