# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest60943(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    kind = 'json' if str(forwarded_ip).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = forwarded_ip
            data = parsed
        case _:
            data = forwarded_ip
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
