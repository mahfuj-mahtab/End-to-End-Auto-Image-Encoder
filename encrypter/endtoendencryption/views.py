from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.core.mail import send_mail  
from random import randint, randrange
from django.contrib.auth import logout
from .models import *
from PIL import Image
# Create your views here.
def home(request):
    print(request.user)
    return render(request,'index.html')
def encodefunc(request):
    if(request.method == 'POST'):
        imgname = request.FILES['imgfile']
        msg = request.POST['msg']
        u = Upload(img = imgname)
        u.save()
        print(imgname)
        print("Hello")
        
        def genData(data):

                # list of binary codes
                # of given data
                newd = []

                for i in data:
                    newd.append(format(ord(i), '08b'))
                return newd

        # Pixels are modified according to the
        # 8-bit binary data and finally returned
        def modPix(pix, data):

            datalist = genData(data)
            lendata = len(datalist)
            imdata = iter(pix)

            for i in range(lendata):

                # Extracting 3 pixels at a time
                pix = [value for value in imdata.__next__()[:3] +
                                        imdata.__next__()[:3] +
                                        imdata.__next__()[:3]]

                # Pixel value should be made
                # odd for 1 and even for 0
                for j in range(0, 8):
                    if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                        pix[j] -= 1

                    elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                        if(pix[j] != 0):
                            pix[j] -= 1
                        else:
                            pix[j] += 1
                        # pix[j] -= 1

                # Eighth pixel of every set tells
                # whether to stop ot read further.
                # 0 means keep reading; 1 means thec
                # message is over.
                if (i == lendata - 1):
                    if (pix[-1] % 2 == 0):
                        if(pix[-1] != 0):
                            pix[-1] -= 1
                        else:
                            pix[-1] += 1

                else:
                    if (pix[-1] % 2 != 0):
                        pix[-1] -= 1

                pix = tuple(pix)
                yield pix[0:3]
                yield pix[3:6]
                yield pix[6:9]

        def encode_enc(newimg, data):
            w = newimg.size[0]
            (x, y) = (0, 0)

            for pixel in modPix(newimg.getdata(), data):

                # Putting modified pixels in the new image
                newimg.putpixel((x, y), pixel)
                if (x == w - 1):
                    x = 0
                    y += 1
                else:
                    x += 1

        # Encode data into image
        def encode():
            # img = input("Enter image name(with extension) : ")
            image = Image.open(imgname, 'r')

            data = msg
            if (len(data) == 0):
                raise ValueError('Data is empty')

            newimg = image.copy()
            encode_enc(newimg, data)

            new_img_name = "en"+str(imgname)
            newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

        # Decode the data in the image
        def decode():
            img = input("Enter image name(with extension) : ")
            image = Image.open(img, 'r')

            data = ''
            imgdata = iter(image.getdata())

            while (True):
                pixels = [value for value in imgdata.__next__()[:3] +
                                        imgdata.__next__()[:3] +
                                        imgdata.__next__()[:3]]

                # string of binary data
                binstr = ''

                for i in pixels[:8]:
                    if (i % 2 == 0):
                        binstr += '0'
                    else:
                        binstr += '1'

                data += chr(int(binstr, 2))
                if (pixels[-1] % 2 != 0):
                    return data

        encode()

      

    return render(request,'decode.html')
def decodefunc(request):
    if(request.method == 'POST'):
        imgname = request.FILES['imgfile']
        # msg = request.POST['msg']
        u = Upload(img = imgname)
        u.save()
        # print(imgname)
        # print("Hello")
        
        def genData(data):

                # list of binary codes
                # of given data
                newd = []

                for i in data:
                    newd.append(format(ord(i), '08b'))
                return newd

        # Pixels are modified according to the
        # 8-bit binary data and finally returned
        def modPix(pix, data):

            datalist = genData(data)
            lendata = len(datalist)
            imdata = iter(pix)

            for i in range(lendata):

                # Extracting 3 pixels at a time
                pix = [value for value in imdata.__next__()[:3] +
                                        imdata.__next__()[:3] +
                                        imdata.__next__()[:3]]

                # Pixel value should be made
                # odd for 1 and even for 0
                for j in range(0, 8):
                    if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                        pix[j] -= 1

                    elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                        if(pix[j] != 0):
                            pix[j] -= 1
                        else:
                            pix[j] += 1
                        # pix[j] -= 1

                # Eighth pixel of every set tells
                # whether to stop ot read further.
                # 0 means keep reading; 1 means thec
                # message is over.
                if (i == lendata - 1):
                    if (pix[-1] % 2 == 0):
                        if(pix[-1] != 0):
                            pix[-1] -= 1
                        else:
                            pix[-1] += 1

                else:
                    if (pix[-1] % 2 != 0):
                        pix[-1] -= 1

                pix = tuple(pix)
                yield pix[0:3]
                yield pix[3:6]
                yield pix[6:9]

 

     
    
        def decode():
            img = imgname
            image = Image.open(img, 'r')

            data = ''
            imgdata = iter(image.getdata())

            while (True):
                pixels = [value for value in imgdata.__next__()[:3] +
                                        imgdata.__next__()[:3] +
                                        imgdata.__next__()[:3]]

                # string of binary data
                binstr = ''

                for i in pixels[:8]:
                    if (i % 2 == 0):
                        binstr += '0'
                    else:
                        binstr += '1'

                data += chr(int(binstr, 2))
                if (pixels[-1] % 2 != 0):
                    return data

        decoded_msg = decode()
        print(decoded_msg)
        return render(request,'DEcodePage.html',{"decoded_msg" : decoded_msg})
    return render(request,'decode.html')
    
def register(request):
    if(request.method == 'POST'):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        email_q = User.objects.all().filter(email = email)
        username_q = User.objects.all().filter(username = username)
        try:
            checked = request.POST['checked']
        except:
            messages.warning(request,'Sorry You Need To Accept The Agreement')
            return render(request,'register.html')
        if(len(firstname) <= 0):
            messages.warning(request,"Sorry First Name Can't be blank")
            return render(request,'register.html')
        else:
            if(len(lastname) <= 0):
                messages.warning(request,"Sorry Last Name Can't be blank")
                return render(request,'register.html')
            else:
                if(len(email_q) == 0):
                    if(len(username_q) == 0):
                        if(len(password) >= 8):
                            user = User.objects.create_user(first_name = firstname,last_name = lastname, username = username,email = email,password = password)
                            user.save()
                            messages.success(request,'We Mailed You With Confirm Code!')
                            code = randint(100000, 999999)
                            request.session['code'] = code
                            request.session['verify'] = email
                            send_mail(
                            'Confirmation Mail',
                            'Here is Your Verification Code {}'.format(code),
                            'itstechnerd@gmail.com',
                            [str(email)],
                            fail_silently=False,
        )
                            return render(request,'verifyprofile.html')
                        #TODO: OTP Auth Need To DO
                        else:
                            messages.warning(request,"Sorry Password Must be 8 Char Long And Must Contain Upper Case Lower Case And Symbol")
                            return render(request,'register.html')
                    else:
                        messages.warning(request,"Sorry Username Already Used")
                        return render(request,'register.html')

                else:
                    messages.warning(request,"Sorry Email Already Used")
                    return render(request,'register.html')

                        
    else:
        return render(request,'register.html')
def loginfunc(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.all().filter(email = email)
        if(len(username) > 0):
            user = authenticate(username = username[0].username,password = password)
            print(user)
        else:
            messages.warning(request,"Sorry Email Or Password Is Wrong!")
            return render(request,'login.html')
        if(user is not None and username[0].is_superuser == False):
            request.session['email'] = email
            login(request,user)
            # return render(request,'login.html')
            return redirect("/")

        else:
            messages.warning(request,"Sorry Email Or Password Is Wrong! hit here")
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def recoverfunc(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        user = User.objects.all().filter(email = email)
        if(len(user) == 1):
            code = randint(100000, 999999)
            request.session['code'] = code
            request.session['verify'] = email
            send_mail(
            'Confirmation Mail',
            'Here is Your Verification Code {}'.format(code),
            'itstechnerd@gmail.com',
            [str(email)],
            fail_silently=False,
        )
            return render(request,'verify.html')
        else:
            messages.warning(request,"Sorry Email Not In Database!")
            return render(request,'Recover.html')            
    else:
        return render(request,'Recover.html')

def verifyfunc(request):
    if(request.method == 'POST'):
        verify = request.POST['verify']
        if(int(verify) == request.session['code']):
            return render(request,'changepass.html')
        else:
            messages.warning(request,"Sorry Verification Code is wrong!")
            return render(request,'verify.html')           
    else:
        return redirect("/account/login")
    
def verifyprofilefunc(request):
    if(request.method == 'POST'):
        verify = request.POST['verify']
        if(int(verify) == request.session['code']):
            user = User.objects.all().filter(email = request.session['verify'])
            messages.success(request,'Registration Success. You Can Login Now!')
            return redirect("/account/login")
        else:
            messages.warning(request,"Sorry Verification Code is wrong!")
            return render(request,'verifyprofile.html')           
    else:
        return redirect("/account/login")
    
def logout_view(request):
    logout(request)
    return redirect("/")