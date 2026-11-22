# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def verify_report(request):
    remark = request.POST.get('field', '')
    if remark:
        note = remark
    else:
        note = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': note})))
