# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import pickle


def BenchmarkTest00229(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    pickle.loads(base64.b64decode(data))
    return JsonResponse({"saved": True})
