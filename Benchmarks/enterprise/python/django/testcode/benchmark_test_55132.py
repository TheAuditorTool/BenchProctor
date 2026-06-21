# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import defusedxml.ElementTree


def BenchmarkTest55132(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
