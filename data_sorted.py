def number_matiere(list):
  List_Matière = []
  for grade in list["grades"]:
      if not grade["Matière"] in List_Matière:
          List_Matière.append(grade["Matière"])
  return {"List_Matière" : List_Matière, "Nombre_Matiere" : len(List_Matière)}


def return_note_matiere(list):
  List_Matière = []
  for matiere in number_matiere(list)["List_Matière"]:
      matiere_temp = []
      for note_info in list["grades"]:
          if note_info["Matière"] == matiere:
              matiere_temp.append({"Note" : note_info["Note"], 
                                   "Coef" : note_info["Coef"], 
                                   "MAX_point" : note_info["MAX_point"]})

      List_Matière.append({"Matière" : matiere, "List_Note" : matiere_temp})

  return List_Matière