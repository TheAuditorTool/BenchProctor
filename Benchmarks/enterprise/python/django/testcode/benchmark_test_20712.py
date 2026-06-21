# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest20712(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = '%s' % (json_value,)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
