# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def BenchmarkTest00972(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = (lambda v: v.strip())(ua_value)
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
