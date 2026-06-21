# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django.http import HttpResponse


def BenchmarkTest08645(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
