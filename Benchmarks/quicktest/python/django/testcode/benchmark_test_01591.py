# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from urllib.parse import unquote


def BenchmarkTest01591(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
