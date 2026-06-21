# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse


def BenchmarkTest41329(request):
    user_id = request.GET.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    return HttpResponse(str(processed), content_type='text/html')
