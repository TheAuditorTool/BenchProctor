# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest76295(request):
    env_value = os.environ.get('USER_INPUT', '')
    trusted_claim = str(env_value)
    return JsonResponse({'trusted': trusted_claim}, status=200)
