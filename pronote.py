import pronotepy
import csv
from datetime import datetime

def log_login(username, password, Work):
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open('login_logs.csv', mode='a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow([timestamp, username, password, Work])


def connect_pronote(username, password):
  try:
    client = pronotepy.Client('https://1320002k.index-education.net/pronote/eleve.html',
                              username=username,
                              password=password)
    #log_login(username, password, True)
    

  except pronotepy.exceptions.AuthenticationError as e:
    print("Invalid username or password. Please try again.")
    error_message = "Invalid Password"
    #log_login(username, password, False)
    return error_message

  somme_coef = 0
  somme_note = 0
  grades = []
  average = 0
  for period in client.periods:
      for grade in period.grades:
        if grade.grade not in ['NonRendu', 'NonNote', 'Absent']:
          note = float(grade.grade.replace(',', '.'))
        
          grades.append({
              'Matière': grade.subject.name,
              'Note': note,
              'Coef': grade.coefficient,
              'MAX_point': grade.out_of,
              'Date': grade.date,
              'Trimestre': grade.period.name
          })
          if float(grade.coefficient) != 0.0:
            somme_note = somme_note + (note * 20) / float(grade.out_of) * float(grade.coefficient)
            somme_coef = somme_coef + float(grade.coefficient)
            average = somme_note / somme_coef
  
  #print("Username : ", username)
  #print("Password : ", password)

  if average < 10:
    looks_like = "Come on, less than 10, you can do better than that"
  elif 10 <= average < 12:
    looks_like = "Not bad, but you can still improve"
  elif 12 <= average < 15:
    looks_like = "Good effort, keep it up"
  elif 15 <= average < 16:
    looks_like = "Great work, you're doing well"
  elif 16 <= average < 18:
    looks_like = "Excellent performance"
  elif 18 <= average < 19:
    looks_like = "Outstanding! You're excelling"
  else:
    looks_like = "Invalid average value or exceptional performance!"

  pronote_info = {
                  "grades" : grades, 
                  "average" : average, 
                  "looks_like" : looks_like, 
                  "name" : client.info.name,
                  "class_name" : client.info.class_name,
                  }
    
  return pronote_info
