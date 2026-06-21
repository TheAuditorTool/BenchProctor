# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03774(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
