from django.shortcuts import render
from django.http import JsonResponse
import json
import random

# Create your views here.
def appView(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        lvl = body_data.get('lvl')

        operation = ["+","-","*","/"]
        string = str(random.randint(1,10**lvl)) + " " + operation[random.randint(0,3)] + " " + str(random.randint(1,100))
        result = eval(string)
        string += " ="
        data = {"string": string, "result": round(result,2)}
        return JsonResponse(data)
    return render(request,"index.html")

