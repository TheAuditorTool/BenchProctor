# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15112(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
