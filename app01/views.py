from django.shortcuts import render


from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.


USER_LIST = []

for i in range(1,999):

    temp = {'name':'root'+str(i),'age':i}
    USER_LIST.append(temp)
#
# def index(request):
#     per_page_count = 10
#     current_page = request.GET.get('p')
#     current_page = int(current_page)
#
#     start = (current_page-1)*per_page_count
#     end = current_page*per_page_count
#
#     data = USER_LIST[start:end]
#
#     return render(request,'index.html',{'user_list':data})

#使用内置分页

def index(request):

    per_page_count = 10
    current_page = request.GET.get('p')
    current_page = int(current_page)

    paginator = Paginator(USER_LIST,10)

    print(paginator.count)  #998 条目总个数
    print(paginator.per_page) #10
    print(paginator.page_range)  #(1,101)
    print(paginator.num_pages)#100页
    # paginator.count    #数据总个数
    # paginator.page()   #page对象
    # paginator.per_page  #每页显示条目数量
    # paginator.page_range  #总页数的索引范围 如（1,10) （1,200）
    #
    # paginator.num_pages #总页数
    #
    return render(request,'index.html',{'user_list':USER_LIST})





