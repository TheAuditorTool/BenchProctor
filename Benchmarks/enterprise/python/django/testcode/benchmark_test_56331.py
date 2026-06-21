# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time


def ensure_str(value):
    return str(value)

def BenchmarkTest56331(request):
    user_id = request.GET.get('id', '')
    data = ensure_str(user_id)
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return JsonResponse({"saved": True})
