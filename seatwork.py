# seatwork bleghhh
from pyscript import display, document

def student_club(e):

        document.getElementById('checking').innerHTML = ''
        student_firstname = document.getElementById('first_name').value
        student_lastname = document.getElementById('last_name').value
        student_fullname = student_firstname + student_lastname
        danceclub_firstnames = ('Isabelle', 'Isabella', 'Leane', 'Jade', 'Sky', 'Stephanie', 'Chalanie', 'Devon', 'Jennifer')
        dcfn1, dcfn2, dcfn3, dcfn4, dcfn5, dcfn6, dcfn7, dcfn8, dcfn9 = danceclub_firstnames

        
        danceclub_lastnames = ('Cabatu', 'Sheng' ,'Gabia', 'Cabatingan', 'Campo', 'Toralde', 'Lumbang', 'Villostas', 'Uy')
        dcln1, dcln2, dcln3, dcln4, dcln5, dcln6, dcln7, dcln8, dcln9 = danceclub_lastnames

        # isa
        fl1 = dcfn1 + dcln1
        # sheng
        fl2 = dcfn2 + dcln2
        # lg
        fl3 = dcfn3 + dcln3
        # jade
        fl4 = dcfn4 + dcln4
        # sky
        fl5 = dcfn5 + dcln5
        # steph (look who it is)
        fl6 = dcfn6 + dcln6
        # chalanie
        fl7 = dcfn7 + dcln7
        # devon
        fl8 = dcfn8 + dcln8
        # jen
        fl9 = dcfn9 + dcln9
        
        danceclub_fullnames = (fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8, fl9)
                
        fullname_checker = student_fullname in danceclub_fullnames
        
        display_message = (f'Sorry {student_firstname} {student_lastname}, you are not apart of or have failed to join OBMC Monarch.. T--T', f'Congratulations {student_firstname} {student_lastname}! You are successfully apart of the dance troupe Monarch, whose club coordinator (and sometimes chereographer) is Sir Akihiro Marutani!! > U <')
        
        display(display_message[fullname_checker], target='checking')
