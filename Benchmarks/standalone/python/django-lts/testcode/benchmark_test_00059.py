# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import pickle


def BenchmarkTest00059(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    pickle.loads(base64.b64decode(data))
    return JsonResponse({"saved": True})
