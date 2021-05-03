from django.shortcuts import render, redirect
# from almondgo.models import Board
# from almondgo.extract import findSentence
'''
from .models import Product
from django.views.generic.edit import FormView
from .forms import RegisterForm
'''

# Create your views here.
# 게시판
'''
def boardView(request):
    template_name = 'almondgo/almondgo.html'
    board_object = Board.objects.all()
    context = {
        'boardobject':board_object
    }
    return render(request, template_name, context)
'''
#첫페이지 
def firstpage(request):
    template_name ='almondgo/firstpage.html'
    return render(request, template_name)

#start2
def start2(request):
    template_name ='almondgo/start2.html'
    return render(request, template_name)

# 예시
def doSomething(request):
    magic=magician.doMagic(request)
    return HttpResponse(magic)

# 정보 처리
def findSentence(request):
    template_name='almondgo/detail.html'
    return render(request,template_name)

# 테스트 페이지
def test(request):
    template_name ='almondgo/test.html'
    return render(request, template_name, context)

# 시작 페이지
def start(request):
    template_name ='almondgo/start.html'
    return render(request, template_name)

# 전체/ 어떤 정보를 보고싶은지 선택하는 화면  
def generalinfo(request):
    template_name ='almondgo/generalinfo.html'
    return render(request,template_name)

# 픽업 서비스
def pick(request):
    template_name='almondgo/pick.html'
    return render(request,template_name)

#서비스 안내
def service(request):
    template_name ='almondgo/service.html'
    return render(request, template_name)
    
#검색 필드
def result(request):
    query = request.GET.get('query')
    global posts
    if query:
        posts = Posts.objects.filter(title__contains='query')
    return render(request, 'result.html',{'Board': Board})

#프랜차이즈 매장 정보
def fmain(request):
    context = {

    }
    return render(request,'almondgo/fmain.html',context=context)

# 메뉴 고르는 화면_ 오프라인 방문 시 특징 정보 
def menupick(request):
    template_name = 'almondgo/menupick.html'
    return render(request, template_name)

# 상품 등록
'''
class Product(FormView):
    template_name ="almondgo/product_register.html"
    form_class = RegisterForm
    success_url="/"

    def form_valid(self,form):
        product = Product (
            name = form.data.get('name'),
            price = form.data.get('price'),
            description = form.data.get('description')
        )
        product.save()
        return super().form_valid(form)
'''


 

