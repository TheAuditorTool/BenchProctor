# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest36501(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
