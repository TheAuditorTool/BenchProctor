# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest42639(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
