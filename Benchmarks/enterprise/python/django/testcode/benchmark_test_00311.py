# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00311(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
