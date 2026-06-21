# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import defusedxml.ElementTree


def BenchmarkTest69914(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
