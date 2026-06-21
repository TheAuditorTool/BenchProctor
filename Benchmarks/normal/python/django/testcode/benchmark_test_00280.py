# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse


def BenchmarkTest00280(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '{}'.format(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    return HttpResponse(str(processed), content_type='text/html')
