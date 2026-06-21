# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def BenchmarkTest40584(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
