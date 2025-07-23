from datetime import datetime
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from basic_form.models import *
import random
import jinja2
import pdfkit


def create_invoice(stdName, bill):
    context = {
        'challanNo':69,
        'studentId':371535,
        'studentName':stdName,
        'fatherName':"Vishal",
        'dept': "SEECS",
        'hostel':"Ghazali",
        'roomNumber':222,
        'messBill': bill,
        'grandTotal':"Free",
        'with5perc':1,
        'with10perc':2,
        'with15perc':3,
        'datewith5perc':"aaj",
        'datewith10perc':"kl",
        'datewith15perc':"prsoon",
        'invoiceDate':"kbhi_bhee",
        'DueDate':"aaj",

        'loc':"https://rb.gy/ns3pkb"}
    for i in range(1,40):
        context[f"ci{i}"] = f"ci_{i}.png"




    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template('trial.html')
    output_text = template.render(context)




    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_string(output_text, f"pdf_{stdName}.pdf", configuration=config, css='style.css')



    

# Create your views here.
@login_required(login_url='/login')
def home(request, notification_id = 0):
    print(notification_id)
    if request.method == "POST":
        if int(notification_id) != 0:
            print("haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaan")
            notice_board.objects.filter(pk = int(notification_id)).delete()
        else:
            msg = request.POST['msg']
            notice_board(msg=msg).save()

        return redirect("/")

    elif request.method == "GET":
        all_msgs = {'total': notice_board.objects.all()}

        # if user is from admin side show him/her notice_board with access of editing it
        if request.user.is_staff:
            return render(request, 'nb_admin.html', context=all_msgs)

        # if user is a student show him/her simple notice_board
        else:
            return render(request, 'notice_board.html', context=all_msgs)


def loginUser(request):
    # create_dummies()
    logout(request)
    # method is POST means ky user login form fill kr chuka hai
    if request.method == "POST":
        # store entered username and password in variables
        username = str(request.POST['username'])
        password = str(request.POST['password'])


        # authenticate entered credentials
        user = authenticate(request, username=username, password=password)

        # if user is valid redirect him/her to home page of website
        if user is not None:
            login(request, user)
            return redirect('/')

        # else show him login page again
    return render(request, 'login.html', context={'user': request.user.username})


# for logging out
def logoutUser(request):
    logout(request)
    return redirect('/login')


# for profile page
@login_required(login_url='/login')
def profile(request):
    # print(notification_id)
    if request.method == "GET":
        # save updated object in a variable
        if request.user.is_staff:

            return render(request, 'profile.html', context={'user': Manager.objects.get(userAccount=request.user), 'flag':1})
        
        else:
            return render(request, 'profile.html', context={'user': Student.objects.get(userAccount=request.user), 'flag':0})

    #
    # if method is post which means user has clicked edit button.
    if request.method == "POST":
        if request.user.is_staff:
            
            userAcc = Manager.objects.filter(userAccount=request.user)

            # if request.POST.get('us')

            for userAcc1 in userAcc:


                newPhoneNumber = userAcc1.phoneNumber if (request.POST['phoneNumber']) == "" else request.POST['phoneNumber']
                newEmail = userAcc1.emailAddress if request.POST['emailAddress'] =="" else request.POST['emailAddress']
                userAcc.update(phoneNumber=newPhoneNumber, emailAddress=newEmail)
       
        else: 
            userAcc = Student.objects.filter(userAccount=request.user)


            for userAcc1 in userAcc:
                newPhNum = userAcc1.phoneNumber if (request.POST['phoneNumber']) == "" else request.POST['phoneNumber']
                newDept = userAcc1.department if (request.POST['dept']) == "" else request.POST['dept']
                newGName = userAcc1.guardianName if (request.POST['GName']) == "" else request.POST['GName']
                newGNumber = userAcc1.guardianPhoneNumber if (request.POST['GNum']) == "" else request.POST['GNum']
                newPAddress = userAcc1.permenantAddress if (request.POST['pAddr']) == "" else request.POST['pAddr']
                userAcc.update(phoneNumber=newPhNum, department=newDept,
                guardianName= newGName, guardianPhoneNumber= newGNumber, permenantAddress= newPAddress)
        return redirect('/profile')


# for invoices
@login_required(login_url='/login')
def invoices(request):
    if request.method == "POST":  # If method is post which means that user has submitted
        """ save invoice"""  # invoice, redirect him/her to homepage
        return redirect('/')

    else:
        if request.user.is_superuser:  # if user is superuser than show him page where he can
            return render(request, 'invoice_dd.html')  # upload invoices

        elif request.user.is_staff:  # manager will be shown page where he can download his hostel's
            # invoice and send it to students' portal

            """ ---------   """
            return HttpResponse('hey manager get the fuck out of here')
            """ ---------  """

        else:  # if user is student, he will be shown a page where he can download his invoice

            """ ---------   """
            return HttpResponse('hey student get the fuck out of here')


@login_required(login_url='/login')
def roomChange(request):
    if request.method == "GET":

        if request.user.is_staff:  # for manager
            return render(request, 'rc_admin.html', context={'object': room_change.objects.all()})

        elif not request.user.is_superuser:  # for student
            return render(request, 'room_change.html')


    else:  # method is post which means user has submitted form
        req_name = request.POST['req_name']
        req_room = int(request.POST['req_room'])
        with_name = request.POST['with_name']
        with_room = int(request.POST['with_room'])

        room_change(req_name= req_name, req_room= req_room, with_name= with_name, with_room= with_room).save()

        # accept ?? button ??

        return redirect('/roomChange')


@login_required(login_url='/login')
def outpass(request):
    if request.method == "POST":

        date_format = '%Y-%m-%d'

        cmsId = int(request.user.username)
      
        # from_date = datetime.datetime.strptime(str(request.POST['fromDate']), date_format)
        from_date = request.POST['fromDate']
        to_date = request.POST['toDate']
        # to_date = datetime.datetime.strptime(str(request.POST['toDate']), date_format)

        reason = request.POST['reason']
        outPass(cmsId = cmsId, From_date=from_date, To_date=to_date, reason=reason).save()
        # accept button
        return redirect('/outpass')

    else:
        if request.user.is_staff:
            
            return render(request, 'outpass_mngr.html',
             context={'object': outPass.objects.all(), 'student': Student.objects})

        else:
            return render(request, 'outPass.html')


@login_required(login_url='/login')
def rAP(request):
    if request.method == "POST":
        print(f"image : {request.POST['img']} \ntype : {type(request.POST['img'])}")

        desc = str(request.POST['desc'])

        obj = rProblems(descrip=desc)
        obj.save()
        return redirect('/report-a-problem')

    else:
        if not request.user.is_superuser:
            if request.user.is_staff:
                return render(request, 'rAP_admin.html', context={'object': rProblems.objects.all()})

            else:
                return render(request, 'RAP.html')
        else:
            return redirect("/")


@login_required(login_url='/login')
def createACC(request):
    
    if request.method == "POST":
        currACC = User.objects.filter(username=str(request.POST['cms_id']))

        if currACC.count():
            currACC.update(password=request.POST['up'])

        else:
            staff_flag = request.user.is_superuser
            newACC = User.objects.create_user(username=str(request.POST['cms_id']), password=str(request.POST['up']),
                                              is_staff=staff_flag)
            if staff_flag:
                name = str(request.POST['cms_id']).split('.')[0]
                Manager(fullName=name, userAccount=newACC).save()
            else:
                Student(cmsId=int(request.POST['cms_id']), userAccount=newACC).save()

            newACC.is_active = True
            newACC.save()

    if request.user.is_superuser:
        return render(request, 'create_mngr.html')
    elif request.user.is_staff:
        return render(request, 'create_user.html')
    else:
        return redirect("/")



def allStudents(request):

    return render(request, 'all_students.html', context={'users':Student.objects.all()})


def allManagers(request):
    return render(request, 'all_managers.html', context={'users':Manager.objects.all()})


def attendance(request):
    # print(randomNumbers)
    stds = Student.objects.all()
    # 
    if request.method =="GET":
        

        sortedStudents = [[],[],[],[]]
        

        for user in stds:
            
            if user.roomNumber > 0:
                sortedStudents[user.roomNumber//100 -1].append(user)

        return render(request, 'attendance_mngr.html', context={'users': sortedStudents})
    
    else:
        a = ["value : "]
        b = ["CMS IDs : "]
        c = ["\nnames : "]
        # for user in stds:
        #     cms = user.cmsId
            
        #     # print(str(request.POST['hey']))
            
            
        #     mark = str(request.POST[str(cms)])
        #     print(mark)
        #     a.append(mark)
        return HttpResponse(request.POST.get("heybro"))
            
            
        #     Attendance(student=user, marking=mark).save()
        
        # return redirect("/")
        return HttpResponse((str(a), str(b), str(c)))
        
def invoicesSubmit(request):
    if request.method == "POST":
    
        # for obj in Hostel.objects.all():
        #     name = obj.get_hostelName_display()
            
        #     name = name+"-"+str(obj.block) if obj.block else name
        #     doc = request.POST[name]
            
            # Invoices(hostelBlockName=obj, monthName=str(request.POST["month"]),
            #  billType=str(request.POST['billType']), invoiceFile = doc)
        Invoices(hostelBlockName="Ghazali-2", monthName=str(request.POST["month"]),
        billType=str(request.POST['billType']), invoiceFile = request.FILES['Ghazali-1']).save()
        f = request.FILES['']
        # with open('../save_invoices/xd.txt', 'wb+') as destination:
        #     for chunk in f.chunks():
        #         destination.write(chunk)

        
    return HttpResponse("hey")


def invoiceCreate(request):
    if request.method == "GET":
        return render(request, 'create_invoice.html')
    
    else:
        mpm = request.POST.get('mpm',354)
        create_invoice("Prithvi", 370)
        return redirect("/")



            

           