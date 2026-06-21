# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import pickle


def relay_value(value):
    return value

def BenchmarkTest07990(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = relay_value(referer_value)
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    pickle.loads(processed.encode('latin-1'))
    return JsonResponse({"saved": True})
