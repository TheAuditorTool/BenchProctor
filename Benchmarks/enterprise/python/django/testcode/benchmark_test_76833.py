# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def BenchmarkTest76833(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
