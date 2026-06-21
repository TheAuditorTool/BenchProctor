# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74105(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
