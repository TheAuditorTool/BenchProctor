# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29709(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
