print ('Please select size of the tumor')
print ('Please write A if size of the lesion is less than 2 cm')
print ('Please write B if size of the lesion is more than than 2 but less than 4cm')
print ('Please write C if size of the lesion is more than 4 cm')


def local_extension (prompt):
    while True:
        user_input = input (prompt)
        if user_input == 'A':
            return 'STAGING is T1'
        elif user_input =='B':
            return 'STAGING is T2'
        elif user_input =='C':
            return 'STAGING is T3'
        elif user_input == 'D':
            return 'STAGING is T4a'
        elif user_input == 'E':
            return 'STAGING is T4b'
        else:
            print("Please enter True or False.")
        
prompt = 'Please select A,B,C,D or E: ' 
print ('Please write D if there is any involvement of larynx, extrinsic muscles of tongue, medial pterygoid, hard palate or mandible')
print ('Please write E if there is any involvement of lateral pterygoid, pterygoid plate, skull base, encasement of ICA or lateral nasopharynx')
print (local_extension (prompt))
