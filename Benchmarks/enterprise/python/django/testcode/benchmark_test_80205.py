# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest80205(request):
    upload_name = request.FILES['upload'].name
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
