# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest48110(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    return HttpResponse(Template(data).render(Context()))
