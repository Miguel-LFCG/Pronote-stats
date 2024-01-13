from random import randint, choice
import datetime

def gen_test_profil():
        test_profil = {'grades': [
            {'Matière': 'HISTOIRE-GEOGRAPHIE', 'Note': randint(0, 20), 'Coef': str(randint(0, 3)), 'MAX_point': '20', 'Date': datetime.date(2023, 9, 8), 'Trimestre': 'Trimestre 1'}, 
            {'Matière': 'MATHS EXPERTES', 'Note': 4.75, 'Coef': '1', 'MAX_point': '5', 'Date': datetime.date(2023, 9, 18), 'Trimestre': 'Trimestre 1'}, 
            {'Matière': 'Mathématiques', 'Note': 13.25, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 9, 21), 'Trimestre': 'Trimestre 1'}, 
            {'Matière': 'MATHS EXPERTES', 'Note': 3.75, 'Coef': '1', 'MAX_point': '7', 'Date': datetime.date(2023, 9, 25), 'Trimestre': 'Trimestre 1'}, 
            {'Matière': 'ANGLAIS LV1', 'Note': 20.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 10, 3), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'ENSEIGNEMENT SCIENTIFIQUE', 'Note': 12.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 10, 9), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'MATHS EXPERTES', 'Note': 3.25, 'Coef': '1', 'MAX_point': '5', 'Date': datetime.date(2023, 10, 9), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'ESPAGNOL 2', 'Note': 14.5, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 10, 6), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'ESPAGNOL 2', 'Note': 13.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 10, 5), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'HISTOIRE-GEOGRAPHIE', 'Note': 12.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 10, 10), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'Mathématiques', 'Note': 13.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 10, 14), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'ESPAGNOL 2', 'Note': 20.0, 'Coef': '2', 'MAX_point': '20', 'Date': datetime.date(2023, 10, 12), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'PHILOSOPHIE', 'Note': 11.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 10, 20), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'NUMÉRIQUE SCIENCES INFORMATIQUES', 'Note': 3.25, 'Coef': '3', 'MAX_point': '5', 'Date': datetime.date(2023, 10, 22), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'NUMÉRIQUE SCIENCES INFORMATIQUES', 'Note': 8.0, 'Coef': '1', 'MAX_point': '8', 'Date': datetime.date(2023, 10, 22), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'NUMÉRIQUE SCIENCES INFORMATIQUES', 'Note': 1.75, 'Coef': '3', 'MAX_point': '5', 'Date': datetime.date(2023, 10, 22), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'PHILOSOPHIE', 'Note': 12.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 11, 7), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'PHILOSOPHIE', 'Note': 10.0, 'Coef': '3', 'MAX_point': '20', 'Date': datetime.date(2023, 11, 11), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'Mathématiques', 'Note': 15.5, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 11, 11), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'ESPAGNOL 2', 'Note': 20.0, 'Coef': '2', 'MAX_point': '20', 'Date': datetime.date(2023, 10, 13), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'NUMÉRIQUE SCIENCES INFORMATIQUES', 'Note': 2.5, 'Coef': '1', 'MAX_point': '8', 'Date': datetime.date(2023, 11, 19), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'ENS. MORAL & CIVIQUE', 'Note': 13.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 11, 21), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'ED.PHYSIQUE & SPORT.', 'Note': 17.4, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 11, 22), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'MATHS EXPERTES', 'Note': 10.0, 'Coef': '0.5', 'MAX_point': '20', 'Date': datetime.date(2023, 11, 20), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'HISTOIRE-GEOGRAPHIE', 'Note': 10.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 11, 24), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'ESPAGNOL 2', 'Note': 16.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 11, 24), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'ESPAGNOL 2', 'Note': 16.0, 'Coef': '3', 'MAX_point': '20', 'Date': datetime.date(2023, 11, 16), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'ESPAGNOL 2', 'Note': 16.0, 'Coef': '2', 'MAX_point': '20', 'Date': datetime.date(2023, 11, 9), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'ED.PHYSIQUE & SPORT.', 'Note': 17.75, 'Coef': '2', 'MAX_point': '20', 'Date': datetime.date(2023, 11, 25), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'ENSEIGNEMENT SCIENTIFIQUE', 'Note': 11.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 11, 26), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'Mathématiques', 'Note': 12.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 11, 27), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'ANGLAIS LV1', 'Note': 20.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 10, 17), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'ANGLAIS LV1', 'Note': 20.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 11, 7), 'Trimestre': 'Trimestre 1'},
            {'Matière': 'HISTOIRE-GEOGRAPHIE', 'Note': 17.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2023, 12, 1), 'Trimestre': 'Trimestre 2'},
            {'Matière': 'MATHS EXPERTES', 'Note': 9.5, 'Coef': '0.5', 'MAX_point': '10', 'Date': datetime.date(2023, 12, 4), 'Trimestre': 'Trimestre 2'},
            {'Matière': 'MATHS EXPERTES', 'Note': 6.25, 'Coef': '1', 'MAX_point': '10', 'Date': datetime.date(2023, 12, 11), 'Trimestre': 'Trimestre 2'},
            {'Matière': 'NUMÉRIQUE SCIENCES INFORMATIQUES', 'Note': 10.0, 'Coef': '1', 'MAX_point': '12', 'Date': datetime.date(2024, 1, 4), 'Trimestre': 'Trimestre 2'},
            {'Matière': 'Mathématiques', 'Note': 13.5, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2024, 1, 4), 'Trimestre': 'Trimestre 2'},
            {'Matière': 'ENSEIGNEMENT SCIENTIFIQUE', 'Note': 9.0, 'Coef': '3', 'MAX_point': '12', 'Date': datetime.date(2024, 1, 7), 'Trimestre': 'Trimestre 2'},
            {'Matière': 'ENSEIGNEMENT SCIENTIFIQUE', 'Note': 18.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2024, 1, 7), 'Trimestre': 'Trimestre 2'},
            {'Matière': 'PHILOSOPHIE', 'Note': 12.0, 'Coef': '1', 'MAX_point': '20', 'Date': datetime.date(2024, 1, 9), 'Trimestre': 'Trimestre 2'},
            # Add the remaining grades here
        ], 'average': 18.5, 'looks_like': 'This is a test version !', 'name': 'Name_TEST', 'class_name': 'Class_TEST'}

        somme_note = 0
        somme_coef = 0
        for grade in test_profil['grades']:
            grade['MAX_point'] = randint(1, 20)
            grade['Note'] = randint(0, grade['MAX_point'])
            grade['Coef'] = randint(0, 3)
            if str(grade["Coef"]) != '0.0' and str(grade["Coef"]) != '0':
              somme_note = somme_note + (grade['Note'] * 20) / float(grade["MAX_point"]) * float(grade['Coef'])
              somme_coef = somme_coef + float(grade['Coef'])
              average = somme_note / somme_coef
        test_profil['name'] = choice(['Bernard', 'Olivier', 'Cedric', 'Elias', 'Mouloud'])
        if test_profil['name'] == 'Mouloud': 
          test_profil['class_name'] = "Terminal 1, direction Bamaco"
        return test_profil


