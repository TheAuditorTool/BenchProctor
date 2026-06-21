# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32920(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
