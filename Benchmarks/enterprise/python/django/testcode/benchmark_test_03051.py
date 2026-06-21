# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def BenchmarkTest03051(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
