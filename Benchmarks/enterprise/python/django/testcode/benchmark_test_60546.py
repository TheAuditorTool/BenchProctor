# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from urllib.parse import unquote


def BenchmarkTest60546(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    return HttpResponse(Template(data).render(Context()))
