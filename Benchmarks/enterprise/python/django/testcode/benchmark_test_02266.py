# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse
import json
import unicodedata


def BenchmarkTest02266(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', graphql_var):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = graphql_var
    normalized = unicodedata.normalize('NFKC', str(processed))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
