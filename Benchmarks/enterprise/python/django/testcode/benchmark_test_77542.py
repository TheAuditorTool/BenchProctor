# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import defusedxml.ElementTree


def BenchmarkTest77542(request):
    env_value = os.environ.get('USER_INPUT', '')
    defusedxml.ElementTree.fromstring(str(env_value))
    return JsonResponse({"saved": True})
