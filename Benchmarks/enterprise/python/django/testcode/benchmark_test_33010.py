# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest33010(request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
