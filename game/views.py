from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">黄金矿工</h1>'
    line4 = '<a href="/play/">进入游戏界面</a>'
    line3 = '<hr>'
    line2 = '<img src="https://img.wb0311.com/uploadimg/img/2020/0901/1598938688505016.jpg" width=2000>'
    return HttpResponse(line1 + line4 + line3 + line2)

def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'
    line3 = '<a href="/">返回主页面</a>'
    line4 = '<hr>'
    line2 = '<img src="https://img.wb0311.com/uploadimg/img/2020/0901/1598938688505016.jpg" width=2000>'
    return HttpResponse(line1 + line3 + line4 + line2)
# Create your views here.
