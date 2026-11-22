# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00081(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    eval(str(processed))
    return JsonResponse({"saved": True})
