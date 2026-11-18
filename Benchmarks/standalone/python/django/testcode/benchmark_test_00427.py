# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import pickle


def BenchmarkTest00427(request):
    field_value = request.POST.get('field', '')
    data = '{}'.format(field_value)
    pickle.loads(base64.b64decode(data))
    return JsonResponse({"saved": True})
