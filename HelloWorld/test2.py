from django.shortcuts import render
from django.views.decorators import csrf
from HelloWorld import os


# 接收POST请求数据
def test2(request):
    ctx = {}
    if request.POST:
        train = request.POST['train']
        tasks= request.POST['task']
        database = request.POST['database']
        model = request.POST['model']
        cmd='python scripts\\'+train+'.py --task '+tasks+'--dataset '+database+' --model '+model
        if train=='parallel_train':
            cmd+= '--device-id 0 --seed 0 1 2 3 4'
        else:
            cmd+='--seed 0 1 2 3 4'
        ctx['rlt']=cmd
        #os.operation(cmd)
    return render(request, "test2.html", ctx)

#python scripts/parallel_train.py --task node_classification --dataset cora --model pyg_gcn pyg_gat --device-id 0 --seed 0 1 2 3 4