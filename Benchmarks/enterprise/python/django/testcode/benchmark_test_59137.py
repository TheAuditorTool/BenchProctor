# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import pickle


def BenchmarkTest59137(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
