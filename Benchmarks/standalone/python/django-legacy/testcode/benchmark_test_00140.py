# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import pickle


def BenchmarkTest00140(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % str(referer_value)
    pickle.loads(base64.b64decode(data))
    return JsonResponse({"saved": True})
