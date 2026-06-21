# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


request_state: dict[str, str] = {}

def BenchmarkTest13233(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    processed = data[:64]
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
