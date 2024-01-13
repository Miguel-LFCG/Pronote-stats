from data_sorted import return_note_matiere

class Coefficients:
  def __init__(self):
      self.coefficients = {
          'Francais': 10,
          'Philosophie': 8,
          'Specialite1': 16,
          'Specialite2': 16,
          'GrandOral': 10,
          'SpecialiteAbandonnee': 8,
          'HistoireGeographie': 6,
          'LangueVivanteA': 6,
          'LangueVivanteB': 6,
          'EnseignementScientifique': 6,
          'EPS': 6,
          'EnseignementMoralCivique': 2
      }

  def calculate_average(self, grades):
      total_points = 0
      total_coef = 0

      for subject, coef in self.coefficients.items():
          if subject in grades:
              total_points += grades[subject] * coef
              total_coef += coef

      if total_coef == 0:
          return 0  # To avoid division by zero

      average = total_points / total_coef
      return average

class Predict_Algo:
  def __init__(self, notes):
    self.notes = return_note_matiere(notes)
    self.notes_list_raw = notes
    
  def Philosophie_gen(self):
    Note_FINAL = 1
    total_coef = 0
    for notes in self.notes:
      if notes['Matière'] == 'PHILOSOPHIE':
        for note in notes['List_Note']:
          coef = int(note['Coef'])
          single_note  = int(note['Note'])
          if coef > 1:
            total_coef += 4
            Note_FINAL += (single_note  * 4)
          elif coef > 0:
            total_coef += 1
            Note_FINAL += (single_note)
          else:
            print("Warning: Coefficient is 0 or negative. Skipping this entry.")
      Note_FINAL += (self.notes_list_raw['average'] * 1)
      total_coef += 1
    return (format(Note_FINAL/total_coef, '.1f'))

  def Specialité_gen(self, nom_spe):
    Note_FINAL = 1
    for notes in self.notes:
      if notes['Matière'] == str(nom_spe):
        for note in notes['List_Note']:
          coef = int(note['Coef'])
          note = int(note['Note'])
          if coef > 1.0:
            Note_FINAL = Note_FINAL * note * coef
          elif coef > 0:
            Note_FINAL = Note_FINAL * note / 2
          else:
            print("Warning: Coefficient is 0 or negative. Skipping this entry.")
    return Note_FINAL