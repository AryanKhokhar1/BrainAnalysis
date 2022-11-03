from datetime import date, datetime
from django.shortcuts import render
from analysis.models import Report,Analyse
# Create your views here.
def home(request):
    if request.method == "POST":
        name= request.POST.get("name")
        college= request.POST.get("college")
        branch= request.POST.get("branch")
        phone= request.POST.get("phone")
        email= request.POST.get("email")
        question1 = request.POST.get("question1")
        question2 = request.POST.get("question2")
        question3 = request.POST.get("question3")
        question4 = request.POST.get("question4")
        question5 = request.POST.get("question5")
        question6 = request.POST.get("question6")
        question7 = request.POST.get("question7")
        question8 = request.POST.get("question8")
        question9 = request.POST.get("question9")
        data = Analyse(name=name,college=college,branch=branch,phone=phone,email=email,question1 = question1,question2 = question2,question3 = question3,question4 = question4,question5 = question5,question6 = question6,question7 = question7,question8 = question8,question9 = question9,date = datetime.today())
        data.save()
        total = int(question1) + int(question2) + int(question3) + int(question4) + int(question5) + int(question6) + int(question7) + int(question8) + int(question9)
        total = total*10
        if(total <=140):
            context = {
                'variable1':"You have a analytical mind",
                'variable2':"You good at multitasking",
                'variable3':"Sharp mind",
                'variable4':"Good at processing big amount of data"
            }
        elif(total <=190):
            context = {
                'variable1':"Creative mind",
                'variable2':"Explorer",
                'variable3':"Love Solving Logical puzzle",
                'variable4':"Want to do something revolutionary"
            }
        elif(total <=240):
            context = {
                'variable1':"Leader Skill",
                'variable2':"Love to Share Knowledge",
                'variable3':"Good consultant",
                'variable4':"You have motivational skill"
            }
        else:
            context = {
                'variable1':"Introvert",
                'variable2':"Love Nature",
                'variable3':"Some unique skill",
                'variable4':"Care pets"
            }
        return render(request,"aftersubmit.html",context)
    else:
        return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def report(request):
    if request.method == "POST":
        name= request.POST.get("name")
        college= request.POST.get("college")
        branch= request.POST.get("branch")
        phone= request.POST.get("phone")
        email= request.POST.get("email")
        problem= request.POST.get("problem")
        report = Report(name = name,college= college,branch= branch,phone = phone,email = email,problem = problem,date = datetime.today())
        report.save()
        return render(request,"successful.html")
    else:
        return render(request,"report.html")