# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23753(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
