# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27838(request):
    multipart_value = request.POST.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
