# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest45174(request):
    upload_name = request.FILES['upload'].name
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', upload_name):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = upload_name
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
