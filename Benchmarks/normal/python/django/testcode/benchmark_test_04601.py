# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04601(request):
    multipart_value = request.POST.get('multipart_field', '')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(multipart_value))
    return JsonResponse({'lookup': arr[idx]}, status=200)
