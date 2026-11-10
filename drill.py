from pyscript import display, document

def adding_newmembers(e):

    document.getElementById('output').innerHTML = ''
    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value
    
    newmember = first_name + ' ' + last_name

    grade7_membersfn = {'Isaiah', 'Sophia', 'Jamil'}
    fn71, fn72, fn73 = grade7_membersfn
    
    grade7_membersln = {'Boominathan', 'Reyes', 'Santos'}
    ln71, ln72, ln73 = grade7_membersln
    
    grade8_membersfn = {'Ameila', 'Jack', 'Edd'}
    fn81, fn82, fn83 = grade8_membersfn

    grade8_membersln = {'Reyes', 'Nolan', 'Gould'}
    ln81, ln82, ln83 = grade8_membersln

    grade9_membersfn = {'Zeus', 'Kent', 'Eliza'}
    fn91, fn92, fn93 = grade9_membersfn

    grade9_membersln = {'Manalo', 'Stopp', 'Dela Cruz'}
    ln91, ln92, ln93 = grade9_membersln

    grade10_membersfn = {'Zack', 'Jose', 'Mercy'}
    fn101, fn102, fn103 = grade10_membersfn

    grade10_membersln = {'Alfarez', 'Fernandez', 'Thompson'}
    ln101, ln102, ln103 = grade10_membersln

#grade7 full names
    fl71 = fn71 + ' ' + ln71
    fl72 = fn72 + ' ' + ln72
    fl73 = fn73 + ' ' + ln73

#grade8 full names
    fl81 = fn81 + ' ' + ln81
    fl82 = fn82 + ' ' + ln82
    fl83 = fn83 + ' ' + ln83

#grade9 full names
    fl91 = fn91 + ' ' + ln91
    fl92 = fn92 + ' ' + ln92
    fl93 = fn93 + ' ' + ln93

#grade10 full names 
    fl101 = fn101 + ' ' + ln101
    fl102 = fn102 + ' ' + ln102
    fl103 = fn103 + ' ' + ln103
    

    grade7_members = (fl71, fl72, fl73)
    grade8_members = (fl81, fl82, fl83)
    grade9_members = (fl91, fl92, fl93)
    grade10_members = (fl101, fl102, fl103)
    all_members = {grade7_members + grade8_members + grade9_members + grade10_members}
    all_members.add(newmember)

    display(all_members, target='output')
    input # wait for the user gosh dang nabit
