from django import forms

class ipform(forms.Form):
    cont=forms.CharField(label='提醒内容')
    stu=forms.CharField(label='注意的同学',required=False)
