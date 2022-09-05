import streamlit as st
import streamlit.components.v1 as stc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app_database import EvalForm
from datetime import datetime


engine = create_engine('sqlite:///app_database.db')
Session = sessionmaker(bind=engine)
sess = Session()


html_temp = """
		<div style="background-color:#35858B;padding:10px;border-radius:10px">
		<h1 style="color:#AEFEFF;text-align:center;">Waraq Healthcare Units Quality Evaluation</h1>
		<h2 style="color:#064663;text-align:center;">Healthcare Evaluation App 👅</h2>
		</div>
		"""
st.set_page_config(page_title="Healthcare Quality Eval App",
                   page_icon=":bar_chart", layout="wide")
stc.html(html_temp)
st.subheader("<p><TT>Supervised By:<a style='text-decoration:nome;color:green' target='_blank'>Dr/ Mostafa Gabr</a<TT></p",unsafe_allow_html=True)
st.markdown("<p><TT>Designed and Developed by <a style='text-decoration:none;color:red' target='_blank' href='https://github.com/r4v3n-dr490n'>Mohamed A. Atti</a></TT></p>", unsafe_allow_html=True)


with st.form('Health Care Quality Evaluation Form'):
    with st.expander("1- Patients Rights Evaluation: "):

        col1, col2 = st.columns([2, 1])
        with col1:
            pt_rights_1 = st.selectbox(
                "Is There any posters about Patient rights and duties in waiting room:",
                options=["0-Not Present", "1-Present but not obvious", "2-Present and Obvious"])

            if pt_rights_1 == "0-Not Present":
                pt_rights1 = 0
            elif pt_rights_1 == "1-Present but not obvious":
                pt_rights1 = 1
            else:
                pt_rights1 = 2
            pt_rights_2 = st.selectbox('Patient identification by name and national ID:',
                                       options=['No', 'Either', 'Both'])

            if pt_rights_2 == 'No':
                pt_rights2 = 0
            elif pt_rights_2 == 'Either':
                pt_rights2 = 1
            else:
                pt_rights2 = 2

            pt_rights_3 = st.selectbox(
                "There is complains and suggestion system:",
                options=['Not Applied',
                         'complain box but not applied', 'Applied']
            )

            if pt_rights_3 == 'Not Applied':
                pt_rights3 = 0
            elif pt_rights_3 == 'complain box but not applied':
                pt_rights3 = 1
            else:
                pt_rights3 = 2

            pt_rights_4 = st.selectbox(
                'There is Health and Social educational Program: ',
                options=('None', 'Present But Not Applied',
                         'Present And Applied')
            )

            if pt_rights_4 == 'None':
                pt_rights4 = 0
            elif pt_rights_4 == 'Present But Not Applied':
                pt_rights4 = 1
            else:
                pt_rights4 = 2

        with col2:
            pt_rights_cons = st.text_area('cons.: ', value='NONE')
            pt_rights_sol = st.text_area('Solutions: ', value='NONE')
            pt_rights_notes = st.text_area('Notes: ', value='NONE')

    with st.expander('Emergency Room Evaluation'):
        col3, col4 = st.columns([1, 2])
        with col3:
            emergency_cons = st.text_area(
                'Cons.: ', key='emer_cons', value='NONE')
            emergency_sol = st.text_area(
                'Solutions: ', key='emer_sol', value='NONE')
            emergency_notes = st.text_area(
                'Notes: ', key='emer_notes', value='NONE')
        with col4:

            emergency1 = st.number_input(
                'There is basic emergency drugs List:',
                min_value=0,
                max_value=2,
                value=1,
                help="0 -> No list, 1 -> List but drugs insufficiency, 2 -> complete and avaliable drugs")
            emergency2 = st.number_input(
                'Emergency Record contains demographic data, diagnosis, treatment',
                min_value=0,
                max_value=2,
                value=0,
                help="0 -> data not complete, 1 -> complete without signature, 2 -> complete with signeture")
            emergency3 = st.number_input(
                'There is a nebulizer',
                min_value=0,
                max_value=2,
                value=1,
                help="0-> None, 1-> present and broken, 2-> present and operating")

            emergency4 = st.number_input(
                'Oxygen source: ',
                min_value=0,
                max_value=2,
                value=1,
                help="0-> None, 1-> present and broken, 2-> present and operating")
            emergency5 = st.number_input(
                'Nurse trained on first Aid',
                min_value=0,
                max_value=2,
                value=2,
                help="0-> None, 2-> present and trained"
            )
    with st.expander("3- Lab"):

        lab_1 = st.selectbox(
            'There is a list of chemicals and danger material and its storage handling:',
            options=['NO List', 'Present but not activated', 'Present and activated'])
        if lab_1 == 'NO List':
            lab1 = 0
        elif lab_1 == 'Present but not activated':
            lab1 = 1
        else:
            lab1 = 2

        lab_2 = st.select_slider(
            'Availability of lab materials and personal safety equipments for at least one month',
            options=['Not Available', 'Available but not enough', 'Available and Enough'])
        if lab_2 == 'Not Available':
            lab2 = 0
        elif lab_2 == 'Available but not enough':
            lab2 = 1
        else:
            lab2 = 2

        lab_3 = st.selectbox(
            'There is a list of all lab equipments',
            options=['No List', 'Present But not maintained', 'Present and Periodically maintained'])
        if lab_3 == 'No List':
            lab3 = 0
        elif lab_3 == 'Present but not maintained':
            lab3 = 1
        else:
            lab3 = 2

        lab_4 = st.selectbox(
            'There is Actual separation between labs of blood and parasitology',
            options=['No Actual separation', 'There is Actual separation'])
        if lab_4 == 'No Actual separation':
            lab4 = 0
        else:
            lab4 = 2

        col5, col6, col7 = st.columns([1, 1, 1])
        with col5:
            lab_cons = st.text_area('Cons.:', key='lab_cons', value='None')
        with col6:
            lab_sol = st.text_area('Solutions:', key='lab_sol', value='None')
        with col7:
            lab_notes = st.text_area('Notes:', key='lab_notes', value='None')
    with st.expander('4- Pharmacy'):
        pharma_1 = st.selectbox(
            'Prescription is fulfilled',
            options=['less than 60%', '60% to 80%', 'more than 80%']
        )
        if pharma_1 == 'less than 60%':
            pharma1 = 0
        elif pharma_1 == 'more than 80%':
            pharma1 = 1
        else:
            pharma1 = 2

        pharma_2 = st.selectbox(
            'Explain to patient about drug usage and side effects',
            options=['None', 'Explained']
        )
        if pharma_2 == 'None':
            pharma2 = 0
        elif pharma_2 == 'Explained':
            pharma2 = 2

        pharma_3 = st.selectbox(
            'There is correct drug storage policy',
            options=['No Policy', 'Present but not applied',
                     'Present and applied']
        )
        if pharma_3 == 'No Policy':
            pharma3 = 0
        elif pharma_3 == 'Present and applied':
            pharma3 = 1
        else:
            pharma3 = 2

        pharma_4 = st.selectbox(
            'There is drugs identification Card',
            options=['None', 'Present for some categories',
                     'Present for all drugs']
        )
        if pharma_4 == 'None':
            pharma4 = 0
        elif pharma_4 == 'Present for some categories':
            pharma4 = 1
        else:
            pharma4 = 2

        pharma_5 = st.selectbox(
            'Highly dangerous and syllable similarities are distinguished',
            options=['No', 'Yes']
        )
        if pharma_5 == 'No':
            pharma5 = 0
        elif pharma_5 == 'Yes':
            pharma5 = 2

        col8, col9, col10 = st.columns([1, 1, 1])
        with col8:
            pharma_cons = st.text_area(
                'Cons',
                key='pharma_cons',
                value='None'
            )
        with col9:
            pharma_sol = st.text_area(
                'Solutions:',
                key='pharma_sol',
                value='None'
            )
        with col10:
            pharma_notes = st.text_area(
                'Notes:',
                key='pharma_notes',
                value='None'
            )
    with st.expander('5- Infection Control'):
        infect_1 = st.selectbox(
            'There is hand wash policy and staff know it and applied',
            options=['No Policy', 'Present But Not Applied',
                     'Present and Applied']
        )
        if infect_1 == 'No Policy':
            infect1 = 0
        elif infect_1 == 'Present But Not Applied':
            infect1 = 1
        else:
            infect1 = 2

        infect_2 = st.selectbox(
            'Sterilization Policy',
            options=['No Policy', 'Present but not Applied',
                     'Present and applied']
        )
        if infect_2 == 'No Policy':
            infect2 = 0
        elif infect_2 == 'Present But Not Applied':
            infect2 = 1
        else:
            infect2 = 2

        infect_3 = st.selectbox(
            'Safe Garbage disposal',
            options=['No Policy', 'Present but not Applied',
                     'Present and applied']
        )
        if infect_3 == 'No Policy':
            infect3 = 0
        elif infect_3 == 'Present But Not Applied':
            infect3 = 1
        else:
            infect3 = 2

        infect_4 = st.selectbox(
            'Cleaning Policy',
            options=['No Policy', 'Present but not Applied',
                     'Present and applied']
        )
        if infect_4 == 'No Policy':
            infect4 = 0
        elif infect_4 == 'Present But Not Applied':
            infect4 = 1
        else:
            infect4 = 2

        infect_5 = st.selectbox(
            'Availability of infection control materials for at least one month',
            options=['Not Available', 'Available but not enough',
                     'Available and Enough']
        )
        if infect_5 == 'Not Available':
            infect5 = 0
        elif infect_5 == 'Available but not enough':
            infect5 = 1
        else:
            infect5 = 2

        infect_6 = st.selectbox(
            'Garbage are separated',
            options=['Not done', 'Partially separated', 'Totally separated']
        )
        if infect_6 == 'Not Done':
            infect6 = 0
        elif infect_6 == 'Partially Separated':
            infect6 = 1
        else:
            infect6 = 2

        col11, col12, col13 = st.columns([1, 1, 1])
        with col11:
            infect_cons = st.text_area(
                'Cons:',
                key='infect_cons',
                value='None'
            )
        with col12:
            infect_sol = st.text_area(
                'Solutions:',
                key='infect_sol',
                value='None'
            )
        with col13:
            infect_notes = st.text_area(
                'Notes',
                key='infect_notes',
                value='None'
            )
    # Environmental Safety
    with st.expander('6- Environmental Safety'):
        enviro_1 = st.selectbox(
            'Building Status',
            options=['last improve more than 10 yrs',
                     'Not structurally well', 'Structurally Well']
        )
        if enviro_1 == 'last improve more than 10 yrs':
            enviro1 = 0
        elif enviro_1 == 'Not structurally well':
            enviro1 = 1
        else:
            enviro1 = 2

        enviro_2 = st.selectbox(
            'Fire Policy',
            options=['No', 'Yes']
        )
        if enviro_2 == 'No':
            enviro2 = 0
        elif enviro_2 == 'Yes':
            enviro2 = 2

        enviro_3 = st.selectbox(
            'There are Schedules for medical and non medical equipments maintenance',
            options=['None', 'Present and not applied', 'Present and applied']
        )
        if enviro_3 == 'None':
            enviro3 = 0
        elif enviro_3 == 'Present and not applied':
            enviro3 = 1
        else:
            enviro3 = 2

        enviro_4 = st.selectbox(
            'There are enough fire appliances and distributed',
            options=['None', 'Less than 5', 'More than 5']
        )
        if enviro_4 == 'None':
            enviro4 = 0
        elif enviro_4 == 'Less than 5':
            enviro4 = 1
        else:
            enviro4 = 2

        enviro_5 = st.selectbox(
            'No Smoking Policy',
            options=['None', 'Present and Not Applied', 'Present and applied']
        )

        if enviro_5 == 'None':
            enviro5 = 0
        elif enviro_5 == 'Present and not applied':
            enviro5 = 1
        else:
            enviro5 = 2

        col14, col15, col16 = st.columns([1, 1, 1])
        with col14:
            enviro_cons = st.text_area(
                'Cons',
                key='enviro_cons',
                value='None'
            )
        with col15:
            enviro_sol = st.text_area(
                'Solutions:',
                key='enviro_sol',
                value='None'
            )
        with col16:
            enviro_notes = st.text_area(
                'Notes',
                key='enviro_notes',
                value='None'
            )
    # dentistry
    with st.expander('7- Dentistry: '):
        dent_1 = st.selectbox(
            'There is full functional Unit',
            options=['Present but not working', 'Present and working']
        )
        if dent_1 == 'Present but not working':
            dent1 = 0
        elif dent_1 == 'Present and working':
            dent1 = 2

        dent_2 = st.selectbox(
            'There is list of offered service',
            options=['None', 'Present but not clear', 'Present and Clear']
        )
        if dent_2 == 'None':
            dent2 = 0
        elif dent_2 == 'Present but not clear':
            dent2 = 1
        else:
            dent2 = 2

        dent_3 = st.selectbox(
            'Availability of materials for at least one month',
            options=['Not Available', 'Available but not enough',
                     'Available and Enough']
        )
        if dent_3 == 'Not Available':
            dent3 = 0
        elif dent_3 == 'Available but not enough':
            dent3 = 1
        else:
            dent3 = 2

        col17, col18, col19 = st.columns([1, 1, 1])
        with col17:
            dent_cons = st.text_area(
                'Cons:',
                key='dent_cons',
                value='None'
            )
        with col18:
            dent_sol = st.text_area(
                'Solutions:',
                key='dent_sol',
                value='None'
            )
        with col19:
            dent_notes = st.text_area(
                'Notes:',
                key='dent_notes',
                value='None'
            )
    # management
    with st.expander('8- Healthcare Management'):
        manage_1 = st.selectbox(
            'There is HR protocol',
            options=['None', 'Present but not updated', 'Present and updated']
        )
        if manage_1 == 'None':
            manage1 = 0
        elif manage_1 == 'Present and updated':
            manage1 = 1
        else:
            manage1 = 2

        manage_2 = st.selectbox(
            'Patient Privacy Signing',
            options=['Less than 50%', '50% to 75%', 'More than 75%']
        )
        if manage_2 == 'Less than 50%':
            manage2 = 0
        elif manage_2 == '50% to 75%':
            manage2 = 1
        else:
            manage2 = 2

        manage_3 = st.selectbox(
            'Uniform commitment',
            options=['Some not committed', 'All are Committed']
        )
        if manage_3 == 'Some not committed':
            manage3 = 0
        elif manage_3 == 'All are Committed':
            manage3 = 2

        manage_4 = st.selectbox(
            'Commitment to Attendance Schedule',
            options=['Absent', '20% Absent', 'No Absence']
        )
        if manage_4 == 'Absent':
            manage4 = 0
        elif manage_4 == '20% Absent':
            manage4 = 1
        else:
            manage4 = 2

        col20, col21, col22 = st.columns([1, 1, 1])
        with col20:
            manage_cons = st.text_area(
                'Cons:',
                key='manage_cons',
                value='None'
            )
        with col21:
            manage_sol = st.text_area(
                'Solutions:',
                key='manage_sol',
                value='None'
            )
        with col22:
            manage_notes = st.text_area(
                'Notes:',
                key='manage_notes',
                value='None'
            )
    # Family medicine
    with st.expander('Family Medicine: '):
        family_1 = st.selectbox(
            'Availability of family medicine novices and folders',
            options=['None', 'Present but not enough', 'Present and enough']
        )
        if family_1 == 'None':
            family1 = 0
        elif family_1 == 'Present but not enough':
            family1 = 1
        else:
            family1 = 2

        family_2 = st.selectbox(
            'Patient Privacy considerations',
            options=['No', 'Yes']
        )
        if family_2 == 'No':
            family2 = 0
        elif family_2 == 'Yes':
            family2 = 2

        family_3 = st.selectbox(
            'Number of Activated Files',
            options=['Less than 50%', '50% to 75%', 'More than 75%']
        )
        if family_3 == 'Less than 50%':
            family3 = 0
        elif family_3 == '50% to 75%':
            family3 = 1
        else:
            family3 = 2

        family_4 = st.selectbox(
            'Continual examination and re-eval in files',
            options=['Less than 50%', '50% to 75%', 'More than 75%']

        )
        if family_4 == 'Less than 50%':
            family4 = 0
        elif family_4 == '50% to 75%':
            family4 = 1
        else:
            family4 = 2

        col23, col24, col25 = st.columns([1, 1, 1])
        with col23:
            family_cons = st.text_area(
                'Cons:',
                key='family_cons',
                value='None'
            )
        with col24:
            family_sol = st.text_area(
                'Solutions:',
                key='family_sol',
                value='None'
            )
        with col25:
            family_notes = st.text_area(
                'Notes:',
                key='family_notes',
                value='None'
            )
    # Mobadarat
    with st.expander('10- Mobadarat S7iah'):
        st.write('New born hearing Examination')
        mobad1 = st.number_input('target:')
        mobad2 = st.number_input('achieve: ')
        # TODO
        mobad_3 = st.selectbox(
            'New born hearing Examination',
            options=['Less than 60%', '60% to 80%', 'More than 80%']
        )
        if mobad_3 == 'Less than 60%':
            mobad3 = 0
        elif mobad_3 == '60% to 80%':
            mobad3 = 1
        else:
            mobad3 = 2

        st.write('Systemic Diseases')
        mobad4 = st.number_input('target:', key='mobad4')
        mobad5 = st.number_input('achieve: ', key='mobad5')
        # TODO
        mobad_6 = st.selectbox(
            'Systemic Diseases',
            options=['Less than 60%', '60% to 80%', 'More than 80%']
        )
        if mobad_6 == 'Less than 60%':
            mobad6 = 0
        elif mobad_6 == '60% to 80%':
            mobad6 = 1
        else:
            mobad6 = 2

        st.write('Woman Health')
        mobad7 = st.number_input('target:', key='mobad7')
        mobad8 = st.number_input('achieve: ', key='mobad8')
        # TODO
        mobad_9 = st.selectbox(
            'Woman Health',
            options=['Less than 60%', '60% to 80%', 'More than 80%']
        )
        if mobad_9 == 'Less than 60%':
            mobad9 = 0
        elif mobad_9 == '60% to 80%':
            mobad9 = 1
        else:
            mobad9 = 2

        st.write('Mother and Baby')
        mobad10 = st.number_input('target:', key='mobad10')
        mobad11 = st.number_input('achieve: ', key='mobad11')
        # TODO
        mobad_12 = st.selectbox(
            'Mother and Baby',
            options=['Less than 60%', '60% to 80%', 'More than 80%']
        )
        if mobad_12 == 'Less than 60%':
            mobad12 = 0
        elif mobad_12 == '60% to 80%':
            mobad12 = 1
        else:
            mobad12 = 2

        col26, col27, col28 = st.columns([1, 1, 1])
        with col26:
            mobad_cons = st.text_area(
                'Cons:',
                key='mobad_cons',
                value='None'
            )
        with col27:
            mobad_sol = st.text_area(
                'Solutions:',
                key='mobad_sol',
                value='None'
            )
        with col28:
            mobad_notes = st.text_area(
                'Notes:',
                key='mobad_notes',
                value='None'
            )
    # Home Isolation Team
    with st.expander('11- Home Isolation Team'):
        isolate_1 = st.selectbox(
            'There are Isolation Teams',
            options=['None', 'Via Phone', 'Home Visits']
        )
        if isolate_1 == 'None':
            isolate1 = 0
        elif isolate_1 == 'Via Phone':
            isolate1 = 1
        else:
            isolate1 = 2

        isolate_2 = st.selectbox(
            'Availability of Pulse Oximeter',
            options=['Not Available', 'Available']
        )
        if isolate_2 == 'Not Available':
            isolate2 = 0
        else:
            isolate_2 = 2

        isolate_3 = st.selectbox(
            'Percent of distributing Pulse Oximeter',

            options=['Less than 60%', '60% to 80%', 'More than 80%']
        )
        if isolate_3 == 'Less than 60%':
            isolate3 = 0
        elif isolate_3 == '60% to 80%':
            isolate3 = 1
        else:
            isolate3 = 2

        col29, col30, col31 = st.columns([1, 1, 1])
        with col29:
            isolate_cons = st.text_area(
                'Cons:',
                key='isolate_cons',
                value='None'
            )
        with col30:
            isolate_sol = st.text_area(
                'Solutions:',
                key='isolate_sol',
                value='None'
            )
        with col31:
            isolate_notes = st.text_area(
                'Notes:',
                key='isolate_notes',
                value='None'
            )
    # 12 Students health services
    with st.expander('12- Student Health Services'):
        stud1 = st.number_input('target:', key='sutd1')
        stud2 = st.number_input('achieve: ', key='stud2')
        # TODO
        stud_3 = st.selectbox(
            'Student Health Services',
            options=['Less than 100%', '100%']
        )
        if stud_3 == 'Less than 100%':
            stud3 = 0
        elif stud_3 == '100%':
            stud3 = 2

        st.write('Students meningitis Vaccination')
        stud4 = st.number_input('target:', key='sutd4')
        stud5 = st.number_input('achieve: ', key='stud5')
        # TODO
        stud_6 = st.selectbox(
            'Students meningitis Vaccination',
            options=['Less than 100%', '100%']
        )
        if stud_6 == 'Less than 100%':
            stud6 = 0
        else:
            stud6 = 2

        col32, col33, col34 = st.columns([1, 1, 1])
        with col32:
            stud_cons = st.text_area(
                'Cons:',
                key='stud_cons',
                value='None'
            )
        with col33:
            stud_sol = st.text_area(
                'Solutions:',
                key='stud_sol',
                value='None'
            )
        with col34:
            stud_notes = st.text_area(
                'Notes:',
                key='stud_notes',
                value='None'
            )

    # 13 New Pregnant women
    col40, col41, col42 = st.columns([1, 1, 1])
    with col40:
        with st.expander('13- Percent of New Pregnant Women benefit from healthcare'):
            new_born1 = st.number_input('Average monthly New born')
            new_preg1 = st.number_input('No of newly pregnant Women')
            # TODO
            preg_1 = st.selectbox(
                'Percent of New Pregnant Women benefit from healthcare',
                options=['Less than 60%', '60% to 80%', 'More than 80%']
            )
            if preg_1 == 'Less than 60%':
                preg1 = 0
            elif preg_1 == '60% to 80%':
                preg1 = 1
            else:
                preg1 = 2

            pregnant_notes = st.text_area(
                'Notes.: ',
                key='pregnant_notes',
                value='None'
            )
    with col41:
        # 14 Average infant visits
        with st.expander('14- Average Infants visits'):
            new_born2 = st.number_input(
                'Average monthly New born',
                key='new_born')
            no_child = st.number_input(
                'No of children have been observed',
                key='no_child')
            # TODO
            child_1 = st.selectbox(
                'Average Child visits ',
                options=['Less than 60%', '60% to 80%', 'More than 80%']
            )
            if child_1 == 'Less than 60%':
                avg_child_visit = 0
            elif child_1 == '60% to 80%':
                avg_child_visit = 1
            else:
                avg_child_visit = 2

            infant_notes = st.text_area(
                'Notes: ',
                key='infant_notes',
                value='None'
            )

    with col42:
        # 15
        with st.expander('15- Percent of New Pregnant Women benefit from healthcare'):
            new_preg2 = st.number_input('Average monthly New Pregnant women')
            new_preg3 = st.number_input('No of Pregnant women whom visits')
            # TODO
            preg_visits = st.selectbox(
                'Percent of Pregnant Women visit healthcare',
                options=['Less than 4', 'More than 4']
            )
            if preg_visits == 'Less than 4':
                avg_preg_visits = 0
            else:
                avg_preg_visits = 2

    col43, col44 = st.columns([1, 1])
    with col43:
        # 16
        with st.expander('Percent of one year infants who carried out hge test'):
            infant1 = st.number_input('No of one year infants')
            infant2 = st.number_input('No of one year infants carried out hge')
            # TODO
            infant_avg = st.selectbox(
                'Percent of one year infants who carried out hge test',
                options=['Less than 60%', '60% to 80%', 'More than 80%']
            )
            if infant_avg == ' Less than 60%':
                infant_avg_hge = 0
            elif infant_avg == '60% to 80%':
                infant_avg_hge = 1
            else:
                infant_avg_hge = 2

            hge_notes = st.text_area(
                'Notes',
                key='hge_notes',
                value='None'
            )
    with col44:
        with st.expander('IMCI'):
            # 17
            is_doctor = st.radio('Doctor Present', options=['Yes', 'No'])
            if is_doctor == 'Yes':
                is_doctor = True
            else:
                is_doctor = False

            st.write('Percent of below 5yrs infants IMCI')
            infant3 = st.number_input('No of below 5yrs infants IMCI')
            infant4 = st.number_input('No of below 5yrs infants')
            # TODO
            imci_avg = st.selectbox(
                'Percent of below 5yrs infants IMCI',
                options=['Less than 60%', '60% to 80%', 'More than 80%']
            )
            if imci_avg == 'Less than 60%':
                avg_imci = 0
            elif imci_avg == '60% to 80%':
                avg_imci = 1
            else:
                avg_imci = 2

            imci_notes = st.text_area(
                'Notes',
                key='imci_notes',
                value='None'
            )
    col45, col46, col47 = st.columns([1, 1, 1])
    with col46:
        submit = st.form_submit_button('Submit Evaluation Data')
    with col47:
        st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)

    if submit:
        try:
            entry = EvalForm(
                evaluator_name="Mohamed A. Atti",
                unit_name='Tanash',
                eval_date=datetime.now(),
                # TODO
                pt_rights1=pt_rights1,
                pt_rights2=pt_rights2,
                pt_rights3=pt_rights3,
                pt_rights4=pt_rights4,
                pt_rights_neg=pt_rights_cons,
                pt_rights_sol=pt_rights_sol,
                pt_rights_notes=pt_rights_notes,
                # TODO Emergency
                emer1=emergency1,
                emer2=emergency2,
                emer3=emergency3,
                emer4=emergency4,
                emer5=emergency5,
                emer_neg=emergency_cons,
                emer_sol=emergency_sol,
                emer_notes=emergency_notes,
                # TODO Lab
                lab1=lab1,
                lab2=lab2,
                lab3=lab3,
                lab4=lab4,
                lab_neg=lab_cons,
                lab_sol=lab_sol,
                lab_notes=lab_notes,
                # TODO Pharmacy
                pharma1=pharma1,
                pharma2=pharma2,
                pharma3=pharma3,
                pharma4=pharma4,
                pharma5=pharma5,
                pharma_neg=pharma_cons,
                pharma_sol=pharma_sol,
                pharma_notes=pharma_notes,
                # TODO Infection Control
                infect1=infect1,
                infect2=infect2,
                infect3=infect3,
                infect4=infect4,
                infect5=infect5,
                infect6=infect6,
                infect_neg=infect_cons,
                infect_sol=infect_sol,
                infect_notes=infect_notes,
                # TODO Environmental Safety
                env1=enviro1,
                env2=enviro2,
                env3=enviro3,
                env4=enviro4,
                env5=enviro5,
                env_neg=enviro_cons,
                env_sol=enviro_sol,
                env_notes=enviro_notes,
                # TODO Dentistry
                dent1=dent1,
                dent2=dent2,
                dent3=dent3,
                dent_neg=dent_cons,
                dent_sol=dent_sol,
                dent_notes=dent_notes,
                # TODO Healthcare Management
                manage1=manage1,
                manage2=manage2,
                manage3=manage3,
                manage4=manage4,
                manage_neg=manage_cons,
                manage_sol=manage_sol,
                manage_notes=manage_notes,
                # TODO Family Medicine
                family1=family1,
                family2=family2,
                family3=family3,
                family4=family4,
                family_neg=family_cons,
                family_sol=family_sol,
                family_notes=family_notes,
                # TODO Mobadarat
                mobad1=mobad1,
                mobad2=mobad2,
                mobad3=mobad3,
                mobad4=mobad4,
                mobad5=mobad5,
                mobad6=mobad6,
                mobad7=mobad7,
                mobad8=mobad8,
                mobad9=mobad9,
                mobad10=mobad10,
                mobad11=mobad11,
                mobad12=mobad12,
                mobad_neg=mobad_cons,
                mobad_sol=mobad_sol,
                mobad_notes=mobad_notes,
                # TODO Home Isolation
                isolate1=isolate1,
                isolate2=isolate2,
                isolate3=isolate3,
                isolate_neg=isolate_cons,
                isolate_sol=isolate_sol,
                isolate_notes=isolate_notes,
                # TODO Students Health Services
                stud1=stud1,
                stud2=stud2,
                stud3=stud3,
                stud4=stud4,
                stud5=stud5,
                stud6=stud6,
                stud_neg=stud_cons,
                stud_sol=stud_sol,
                stud_notes=stud_notes,
                # TODO Pregnant Women
                new_born1=new_born1,
                new_preg1=new_preg1,
                preg1=preg1,
                preg_notes=pregnant_notes,
                # TODO Average infants visits
                new_born2=new_born2,
                no_child=no_child,
                avg_child_visit=avg_child_visit,
                infants_notes=infant_notes,
                # TODO Percentage of Pregnant Women
                new_preg2=new_preg2,
                new_preg3=new_preg3,
                avg_preg_visit=avg_preg_visits,
                # TODO Percentage of 1yr children
                infant1=infant1,
                infant2=infant2,
                avg_infant_hge=infant_avg_hge,
                hge_notes=hge_notes,
                # TODO IMCI
                is_doctor=is_doctor,
                infant3=infant3,
                infant4=infant4,
                imci_avg=avg_imci,
                imci_notes=imci_notes
            )
            sess.add(entry)
            sess.commit()
            st.success('Evaluation Data Submitted Successfully!',
                       icon="✅",)
            st.balloons()
        except Exception as e:
            st.error("Error while submitting evaluation: {}".format(e))
