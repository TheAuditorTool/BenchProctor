# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import pickle


def BenchmarkTest00206(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = (lambda v: v.strip())(auth_header)
    pickle.loads(base64.b64decode(data))
    return JsonResponse({"saved": True})
