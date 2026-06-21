# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import unquote


def BenchmarkTest09630(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    return redirect(str(data))
