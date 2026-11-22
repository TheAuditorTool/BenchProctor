# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import numpy as np


def BenchmarkTest00021(request):
    cookie_value = request.COOKIES.get('session_token', '')
    quantity = int(str(cookie_value))
    total_cents = np.int32(quantity) * np.int32(1999)
    return JsonResponse({'total_cents': int(total_cents)}, status=200)
