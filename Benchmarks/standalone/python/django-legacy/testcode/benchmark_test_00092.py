# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import numpy as np
import os
import json


def BenchmarkTest00092(request):
    env_value = os.environ.get('APP_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    quantity = int(str(data))
    total_cents = np.int32(quantity) * np.int32(1999)
    return JsonResponse({'total_cents': int(total_cents)}, status=200)
