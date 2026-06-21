# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def BenchmarkTest56604(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = header_value if header_value else 'default'
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
