from django.shortcuts import render

def result_page(request):
    # 현재 아무런 추가 데이터를 전달하지 않고 단순 결과 페이지를 렌더링합니다.
    return render(request, 'kakaomapapi/index.html')