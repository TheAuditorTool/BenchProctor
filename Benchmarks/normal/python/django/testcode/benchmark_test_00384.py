# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00384(request):
    multipart_value = request.POST.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
