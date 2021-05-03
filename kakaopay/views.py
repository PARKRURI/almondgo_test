from django.shortcuts import render, redirect
import json
import requests



# Create your views here.
# 결제 준비
def index(request):
    if request.method == "POST":
        URL = "https://kapi.kakao.com/v1/payment/ready"
        headers = {
            "Authorization": "KakaoAK 02d2b9e1ce766cb52a847a805897b317",  
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  
        }
        params = {
            "cid": "TC0ONETIME",    # 단건 결제 테스트용 코드
            "partner_order_id": "1001",     # 주문번호
            "partner_user_id": "german",    # 아이디
            "item_name": "상하이버거",        # 구매 물품 이름
            "quantity": "1",                # 구매 물품 수량
            "total_amount": "6000",        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": "http://almondgotest.pythonanywhere.com/approval/", # 결제 승인 시 이동할 페이지 
            "cancel_url": "http://almondgotest.pythonanywhere.com/cancel/",
            "fail_url": "http://almondgotest.pythonanywhere.com/fail",
        }

        res = request.post(URL, headers=headers, params=params)
        request.session['tid']  = res.json()['tid']  # 결제 승인시 사용할  tid를 세션에 저장
        next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장
        return redirect(next_url)



    return render(request, 'kakaopay/index.html')
    
# 결제 승인
def approval(request):
    URL = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK 02d2b9e1ce766cb52a847a805897b317",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",    # 단건 결제 테스트용 코드
        "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": "1001",     # 주문번호
        "partner_user_id": "german",    # 아이디
        "pg_token": request.GET.get("pg_token"),     # 쿼리 스트링으로 받은 pg토큰
        
    }

    res = requests.post(URL, headers=headers, params=params)
    
    res = res.json()
    context = {
        'res': res,  
        
         
    }
    return render(request, 'kakaopay/approval.html', context)


