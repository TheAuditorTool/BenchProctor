# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest16510(request):
    user_id = request.GET.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(user_id)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = user_id
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
