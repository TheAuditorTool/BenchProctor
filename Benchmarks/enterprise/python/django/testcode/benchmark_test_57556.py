# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest57556(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
