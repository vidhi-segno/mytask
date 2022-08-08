import re
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .form import UserInputForm
from project1 import form
import math
def ans_form(request):
    template_name = 'project1/index.html'
    valuess = Width.objects.values_list('width',flat=True)
    valuess = list(valuess)
    form = UserInputForm()
    if request.method == 'POST':
        form = UserInputForm(data=request.POST)
        if form.is_valid():
            
            b = form.cleaned_data.get('b')
            import math

            inputt=[2000,2500,3000,4000]
            result=[]
            def check(target,arr=[],sum=0,id=0):
                if(sum>target):
                    return 
                if sum==target:
                    result.extend(arr)
                    return
                for i in range(id,len(inputt)):
                    arr.append(inputt[i])
                    check(target,arr,sum+inputt[i],i)
                    arr.pop(len(arr)-1)


            final_result=[]
            user_input = form.save(commit=True)
            target = form.cleaned_data.get('a')

            if target<=max(inputt):
                if target<=2000:
                    final_result=[2000]
                elif target>2000 and target<=2500:
                    final_result=[2500]
                elif target>2500 and target<=3000:
                    final_result=[3000]
                else:
                    final_result=[4000]

            elif len([i for i in inputt if target%i==0]) != 0:
                minn=math.inf
                for i in inputt:
                    if target%i==0:
                        if minn>target//i:
                            minn = target//i
                        result.append([i]*minn) 
                        final_result.append(result)

            elif target%500==0:
                check(target)
                sum=0
                j=0
                for i in range(len(result)):
                    sum+=result[i]
                    if sum==target:
                        final_result.append(result[j:i+1])
                        j=i+1
                        sum=0         

            else:
                a = target%500
                b = 500-a
                c = target+b
                check(c)

                final_result =[]
                sum=0
                j=0
                for i in range(len(result)):
                    sum+=result[i]
                    if sum==c:
                        final_result.append(result[j:i+1])
                        j=i+1
                        sum=0
            
            return render(request, template_name, {'output': final_result[len(final_result)-1],
                                              'msg': True,
                                              'form':form})
    return render(request,template_name,{'form':form})



