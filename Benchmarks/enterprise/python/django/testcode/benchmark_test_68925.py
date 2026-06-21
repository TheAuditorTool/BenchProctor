# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest68925(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    return HttpResponse(Template(data).render(Context()))
