# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


request_state: dict[str, str] = {}

def BenchmarkTest09410(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return JsonResponse({"saved": True})
