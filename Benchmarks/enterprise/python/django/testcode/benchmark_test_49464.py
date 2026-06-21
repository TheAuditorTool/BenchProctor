# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49464(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
