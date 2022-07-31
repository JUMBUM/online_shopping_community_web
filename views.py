from django import http
from django.shortcuts import render
from django.http import HttpResponse
import houseapp.model_df.mainscrap as ms
import houseapp.model_df.today as tdy
import houseapp.model_df.deal as deeaal
import houseapp.model_df.keyword as keyw
import houseapp.model_df.popularpd as ppdd
import houseapp.model_df.mainwriting as mw
import houseapp.model_df.category as cate
import houseapp.model_df.comu as ct
# Create your views here.


def test(requset):
    return HttpResponse('<u>Test</u>')

def test2(requset):
    return render(requset,
                    "houseapp/index.html",{})
    
def store_main(requset):
    return render(requset,
                    "houseapp/store.html",{})
    
def login(requset):
    return render(requset,
                    "houseapp/login.html",{})
    
def find_id(requset):
    return render(requset,
                    "houseapp/id_find.html",{})
    
def find_pw(requset):
    return render(requset,
                    "houseapp/01_find_pw.html",{})
def find_pw2(requset):
    return render(requset,
                    "houseapp/02_find_pw.html",{})
def find_pw3(requset):
    return render(requset,
                    "houseapp/03_find_pw.html",{})           
               

def view_mainscrap(request):
    td = tdy.get_today()
    
    context = {"td":td.to_html}
    return render(request,
                    "houseapp/mainscrap.html",
                    context)
    
        
def view_mainscrap(request):
    df = ms.getCart_list()
    
    context = {"df":df.to_html}
    return render(request,
                    "houseapp/mainscrap.html",
                    context)

    
def view_mainscrap(request):
    df = ms.getCart_list()
    td = tdy.get_today()
    dl = deeaal.get_deal()
    
    context = {"df":df.to_html,"td":td.to_html, "dl":dl.to_html}
    return render(request,
                    "houseapp/mainscrap.html",
                    context)


def view_store_home(request):
    df = ms.getCart_list()
    td = tdy.get_today()
    dl = deeaal.get_deal()
    kw = keyw.get_keyword()
    ppd = ppdd.get_populpd()
    ht = keyw.get_hashtag()
    
    context = {"df":df.to_html,"td":td.to_html, "dl":dl.to_html, "kw":kw.to_html, "ppd":ppd.to_html, "ht":ht.to_html}
    return render(request,
                    "houseapp/store_home.html",
                    context)

def view_hashtag(request):
    ht = keyw.get_hashtag()
    
    context = {"ht":ht.to_html}
    return render(request,
                    "houseapp/hashtag.html",
                    context)

def view_hashtag2(request):
    ht2 = keyw.get_hashtag2()
    
    context = {"ht2":ht2.to_html}
    return render(request,
                    "houseapp/hashtag2.html",
                    context)
    

def view_mw(request):
    mwpn = mw.get_postname_mw()
    mwcm = mw.get_postcomm_mw()
    mwcm2 = mw.get_postcomm_mw2()
    mwcm3 = mw.get_postcomm_mw3()
        
    context = {"mwpn":mwpn, "mwcm":mwcm, "mwcm2":mwcm2, "mwcm3":mwcm3}
    return render(request,
                    "houseapp/mainwriting.html",
                    context)
    
def view_hashtag_main(request):
    kw = keyw.get_keyword()
    
    context = {"kw":kw.to_html}
    return render(request,
                    "houseapp/hashtag_main.html",
                    context)
    
    
def view_category(requset):
    return render(requset,
                    "houseapp/category.html",{})
    
def view_category_gagu(request):
    categg = cate.get_category_gagu()
    
    context = {"categg":categg.to_html}
    return render(request,
                    "houseapp/category_gagu.html",
                    context)

def view_category_deco(request):
    catedc = cate.get_category_deco()
    
    context = {"catedc":catedc.to_html}
    return render(request,
                    "houseapp/category_deco.html",
                    context)
    
def view_category_fabr(request):
    catefb = cate.get_category_fabr()
    
    context = {"catefb":catefb.to_html}
    return render(request,
                    "houseapp/category_fabr.html",
                    context)
    
def view_category_gaju(request):
    categj = cate.get_category_gaju()
    
    context = {"categj":categj.to_html}
    return render(request,
                    "houseapp/category_gaju.html",
                    context)
    
def view_category_jomy(request):
    catejm = cate.get_category_jomy()
    
    context = {"catejm":catejm.to_html}
    return render(request,
                    "houseapp/category_jomy.html",
                    context)
    
def view_category_juba(request):
    catejb = cate.get_category_juba()
    
    context = {"catejb":catejb.to_html}
    return render(request,
                    "houseapp/category_juba.html",
                    context)
    
def view_category_sang(request):
    catesa = cate.get_category_sang()
    
    context = {"catesa":catesa.to_html}
    return render(request,
                    "houseapp/category_sang.html",
                    context)
    
def view_category_suna(request):
    catesn= cate.get_category_suna()
    
    context = {"catesn":catesn.to_html}
    return render(request,
                    "houseapp/category_suna.html",
                    context)

def comu_follow(request) :
    df = ct.posttop1()
    df1_1 = ct.postmid1()
    df1 = ct.postbot1()
    df2 = ct.posttop2()
    df3 = ct.postbot2()
    df4 = ct.posttop3()
    df5 = ct.postbot3()
    df6 = ct.posttop4()
    df7 = ct.postbot4()
    context = { "df" : df, "df1_1" : df1_1, "df1" : df1, "df2" : df2, "df3" : df3, "df4" : df4, "df5" : df5, "df6" : df6, "df7" : df7}
    return render(request,
                    "houseapp/comu_follow.html",
                    context)    
    
def comu_gal_recent(request):
    df8 = ct.gal1()
    df9 = ct.gal2()
    df10 = ct.gal3()
    df11 = ct.gal4()
    context = { "df8" : df8, "df9" : df9, "df10" : df10, "df11" : df11}
    return render(request,   
                    "houseapp/comu_gal_recent.html", 
                    context)  

def comu_gal_best(request):
    df12 = ct.gal5()
    df13 = ct.gal6()
    df14 = ct.gal7()
    df15 = ct.gal8()
    context = { "df12" : df12, "df13" : df13, "df14" : df14, "df15" : df15}
    return render(request,   
                    "houseapp/comu_gal_best.html", 
                    context)  
    
def comu_post_gk1234(request):
    df16 = ct.gk1234main()
    df17 = ct.gk1234prod()
    df18 = ct.gk1234com1()
    context = { "df16" : df16, "df17" : df17, "df18" : df18}
    return render(request,   
                    "houseapp/comu_post_gk1234.html", 
                    context)  
def comu_post_gk1235(request):
    df19 = ct.gk1235main()
    df20 = ct.gk1235prod()
    df21 = ct.gk1235com1()
    context = { "df19" : df19, "df20" : df20, "df21" : df21}
    return render(request,   
                    "houseapp/comu_post_gk1235.html", 
                    context)  
def comu_post_gk1237(request):
    df22 = ct.gk1237main()
    df23 = ct.gk1237prod()
    df24 = ct.gk1237com1()
    context = { "df22" : df22, "df23" : df23, "df24" : df24}
    return render(request,   
                    "houseapp/comu_post_gk1237.html", 
                    context)  
def comu_post_gk1238(request):
    df25 = ct.gk1238main()
    df26 = ct.gk1238prod()
    df27 = ct.gk1238com1()
    context = { "df25" : df25, "df26" : df26, "df27" : df27}
    return render(request,   
                    "houseapp/comu_post_gk1238.html", 
                    context)      