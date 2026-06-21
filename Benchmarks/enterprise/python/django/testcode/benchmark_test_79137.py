# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest79137(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
