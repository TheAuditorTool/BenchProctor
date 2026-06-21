# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def BenchmarkTest51376(request):
    raw_body = request.body.decode('utf-8')
    data = '{}'.format(raw_body)
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
