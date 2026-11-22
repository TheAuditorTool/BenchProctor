# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import pickle


def BenchmarkTest00093(request):
    raw_body = request.body.decode('utf-8')
    data = '{}'.format(raw_body)
    pickle.loads(base64.b64decode(data))
    return JsonResponse({"saved": True})
