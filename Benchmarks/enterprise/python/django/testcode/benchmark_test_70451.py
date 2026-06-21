# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest70451(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    return HttpResponse(Template(data).render(Context()))
