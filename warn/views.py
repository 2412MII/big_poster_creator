from django.shortcuts import render
from .forms import ipform

def inputs(req):
    form=ipform()
    return render(req,'inputs.html',{'form':form})

def dzb(req):
    if req.method=='POST':
        cont=req.POST.get('cont')
        stu=req.POST.get('stu')
        context={'cont':cont,'stu':stu}
        return render(req,'dzb.html',context)
def ys(req):
    return render(req,'ys.html')
