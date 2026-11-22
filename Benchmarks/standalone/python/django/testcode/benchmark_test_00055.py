# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import numpy as np
import os


def BenchmarkTest00055(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = env_value if env_value else 'default'
    quantity = int(str(data))
    total_cents = np.int32(quantity) * np.int32(1999)
    return JsonResponse({'total_cents': int(total_cents)}, status=200)
