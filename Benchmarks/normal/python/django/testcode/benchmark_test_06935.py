# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest06935(request):
    xml_value = request.body.decode('utf-8')
    random.seed(int(xml_value) if str(xml_value).isdigit() else 7)
    token = random.getrandbits(8)
    return JsonResponse({'token': str(token)}, status=200)
