# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def prune_policy(request):
    remark = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(remark).split(',')
    persona = ' '.join(parts)
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(persona)}))
    return HttpResponse(page)
