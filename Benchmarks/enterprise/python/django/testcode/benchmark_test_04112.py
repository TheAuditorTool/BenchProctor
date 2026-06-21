# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest04112(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    return HttpResponse(Template(data).render(Context()))
