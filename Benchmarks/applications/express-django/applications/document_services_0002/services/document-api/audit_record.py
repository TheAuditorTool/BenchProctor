# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def audit_record(request):
    wording = request.GET.get('id', '')
    parts = []
    for token in str(wording).split(','):
        parts.append(token.strip())
    addendum = ','.join(parts)
    subprocess.run(['echo', addendum], shell=False)
    return JsonResponse({"saved": True})
