from django.shortcuts import render
from django.views.decorators import csrf
from HelloWorld import os


# 接收POST请求数据
def test1(request):
    ctx = {}
    if request.POST:
        train="train"
        if request.POST.get("train"):
            train="parallel_train"
        tasks= request.POST['tasks']
        database = request.POST['dataset']
        model = request.POST['model']
        seeds = request.POST['seeds']
        cmd='python scripts\\'+train+'.py --task '+tasks+' --dataset '+database+' --model '+model
        if train=='parallel_train':
            cmd+= '    --device-id 0'
        cmd+='  --seed '
        # ctx['rlt']=os.operation(cmd)
        i=0
        while i<int(seeds):
            cmd+=(str(i)+" ")
            i+=1
        ctx['rlt'] = os.operation(cmd)
    return render(request, "new_test.html", ctx)

#python scripts/parallel_train.py --task node_classification --dataset cora --model pyg_gcn pyg_gat --device-id 0 --seed 0 1 2 3 4