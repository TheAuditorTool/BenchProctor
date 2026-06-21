# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def BenchmarkTest29118(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    pickle.loads(auth_header.encode('latin-1'))
    return JsonResponse({"saved": True})
