# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def archive_bundle(request):
    preface = request.GET.get('id', '')
    parts = []
    for token in str(preface).split(','):
        parts.append(token.strip())
    addendum = ','.join(parts)
    subprocess.run(['echo', addendum], shell=False)
    return JsonResponse({"saved": True})
