# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14300(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
