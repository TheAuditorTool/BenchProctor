# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest03106(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
