# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest35306(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    json.loads(data)
    return JsonResponse({"saved": True})
