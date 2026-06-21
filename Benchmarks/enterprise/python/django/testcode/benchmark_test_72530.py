# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest72530(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    random.seed(int(referer_value) if str(referer_value).isdigit() else 7)
    token = random.getrandbits(8)
    return JsonResponse({'token': str(token)}, status=200)
