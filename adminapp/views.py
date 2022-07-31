from django.shortcuts import render
from django.http import HttpResponse
import adminapp.model_admin.admin as admin

# Create your views here.
def test(request):
    return HttpResponse('<u>test</u>')

def admin_main(requset):
    df = admin.getCart_list()
    td = admin.get_today()
    dl = admin.get_deal()
    
    context = {"df":df.to_html,"td":td.to_html, "dl":dl.to_html}
    return render(requset,
                    "adminapp/admin_main.html",
                        context)    
    
def admin_store(requset):
    df = admin.getCart_list()
    td = admin.get_today()
    dl = admin.get_deal()
    kw = admin.get_keyword()
    ppd = admin.get_populpd()
    ht = admin.get_hashtag()
    
    context = {"df":df.to_html,"td":td.to_html, "dl":dl.to_html, "kw":kw.to_html, "ppd":ppd.to_html, "ht":ht.to_html}
    return render(requset,
                    "adminapp/admin_store_main.html",
                        context)    
                    
def admin_login(requset):
    return render(requset,
                    "adminapp/admin_login.html",{})    

def admin_find_id(requset):
    return render(requset,
                    "adminapp/admin_find_id.html",{})    
    
def admin_find_pw(requset):
    return render(requset,
                    "adminapp/admin_01_find_pw.html",{})      
def admin_find_pw02(requset):
    return render(requset,
                    "adminapp/admin_02_find_pw.html",{})
def admin_find_pw03(requset):
    return render(requset,
                    "adminapp/admin_03_find_pw.html",{})              
    
def admin_pay(requset):
    adf = admin.get_admin_payment()
    context = {"adf" : adf.to_html}
    
    return render(requset,
                    "adminapp/admin_payment.html",
                        context)    

def admin_product(requset):
    adp = admin.get_admin_product()
    context = {"adp" : adp.to_html}
    
    return render(requset,
                    "adminapp/admin_product.html",
                        context)    
    
def admin_stock(requset):
    ads = admin.get_admin_stock()
    context = {"ads" : ads.to_html}
    
    return render(requset,
                    "adminapp/admin_stock.html",
                        context)    
    
def admin_delivery(requset):
    add = admin.get_admin_delivery()
    context = {"add" : add.to_html}
    
    return render(requset,
                    "adminapp/admin_delivery.html",
                        context)    
    
def admin_member(requset):
    admi = admin.get_admin_mem_info()
    context = {"admi" : admi.to_html}
    
    return render(requset,
                    "adminapp/admin_mem_info.html",
                        context)    
    
def admin_seller(requset):
    adsi = admin.get_admin_sel_info()
    context = {"admi" : adsi.to_html}
    
    return render(requset,
                    "adminapp/admin_sel_info.html",
                        context)    
    
def admin_post(requset):
    adpost = admin.get_admin_post()
    adcom = admin.get_admin_comments()
    context = {"adpost" : adpost.to_html, "adcom" : adcom.to_html}
    
    return render(requset,
                    "adminapp/admin_post.html",
                        context)    

def admin_notice(requset):
    adnot = admin.get_admin_notice()
    context = {"adnot" : adnot.to_html}
    
    return render(requset,
                    "adminapp/admin_notice.html",
                        context)    
def comu_follow(request) :
    df = admin.posttop1()
    df1_1 = admin.postmid1()
    df1 = admin.postbot1()
    df2 = admin.posttop2()
    df3 = admin.postbot2()
    df4 = admin.posttop3()
    df5 = admin.postbot3()
    df6 = admin.posttop4()
    df7 = admin.postbot4()
    context = { "df" : df, "df1_1" : df1_1, "df1" : df1, "df2" : df2, "df3" : df3, "df4" : df4, "df5" : df5, "df6" : df6, "df7" : df7}
    return render(request,
                    "adminapp/comu_follow.html",
                    context)    
    
def comu_gal_recent(request):
    df8 = admin.gal1()
    df9 = admin.gal2()
    df10 = admin.gal3()
    df11 = admin.gal4()
    context = { "df8" : df8, "df9" : df9, "df10" : df10, "df11" : df11}
    return render(request,   
                    "houseapp/comu_gal_recent.html", 
                    context)  

def comu_gal_best(request):
    df12 = admin.gal5()
    df13 = admin.gal6()
    df14 = admin.gal7()
    df15 = admin.gal8()
    context = { "df12" : df12, "df13" : df13, "df14" : df14, "df15" : df15}
    return render(request,   
                    "houseapp/comu_gal_best.html", 
                    context)  
    
def comu_post_gk1234(request):
    df16 = admin.gk1234main()
    df17 = admin.gk1234prod()
    df18 = admin.gk1234com1()
    context = { "df16" : df16, "df17" : df17, "df18" : df18}
    return render(request,   
                    "houseapp/comu_post_gk1234.html", 
                    context)  
def comu_post_gk1235(request):
    df19 = admin.gk1235main()
    df20 = admin.gk1235prod()
    df21 = admin.gk1235com1()
    context = { "df19" : df19, "df20" : df20, "df21" : df21}
    return render(request,   
                    "houseapp/comu_post_gk1235.html", 
                    context)  
def comu_post_gk1237(request):
    df22 = admin.gk1237main()
    df23 = admin.gk1237prod()
    df24 = admin.gk1237com1()
    context = { "df22" : df22, "df23" : df23, "df24" : df24}
    return render(request,   
                    "houseapp/comu_post_gk1237.html", 
                    context)  
def comu_post_gk1238(request):
    df25 = admin.gk1238main()
    df26 = admin.gk1238prod()
    df27 = admin.gk1238com1()
    context = { "df25" : df25, "df26" : df26, "df27" : df27}
    return render(request,   
                    "houseapp/comu_post_gk1238.html", 
                    context)  