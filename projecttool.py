import requests

import hashlib



def check_password(password):

    ###################

    #نعرف الدالة الرئيسية الي رح تفحصلنه كلمات المرور



    # هنا شي اكيد رح نحتاج الى تشفير كلمة المرور ونجزئها لغرض الامان

    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    prefix = sha1_password[:5]  # أول 5 احرف

    suffix = sha1_password[5:]  # باقي الاحرف



    # هنا رح يبدي دور ال api

    #  نرسل طلب نمرر من خلاله اول خمس احرف

    #وورا الباقي

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    response = requests.get(url)



    # هنا حيتم عملية البحث هل الجزء الثاني من التشفير مسرب بداخل قاعدة البيانات لو لا

    for line in response.text.splitlines():

        # نفصل كل سطر إلى جزئين: التسريب وعدد مرات التسريب

        pwned_suffix, count = line.split(':')



        # اذا وجدنا تطابق فيعني كلمة المرور مسربة

        if pwned_suffix == suffix:

            # تم تعديل رسالة الخطأ لتكون أوضح

            print(" كلمة المرور مسربة.")

            return



    # إذا انتهى البحث ولم نجد تطابقاً، فهي آمنة

    print(" روح والهوى بضهرك")



# نسوي input حته ندخل بي كلمة المرور

my_password = input("  دخل كلمة المرور مالتك يا بطل : ")



# نستدعي الدالة ونمررلها كلمة المرور لدخلناها

check_password(my_password)