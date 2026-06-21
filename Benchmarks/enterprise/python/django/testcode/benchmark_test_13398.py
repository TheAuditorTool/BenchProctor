# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse
import unicodedata


def BenchmarkTest13398(request):
    xml_value = request.body.decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
