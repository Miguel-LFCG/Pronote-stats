from flask import Flask, render_template, request, flash
from data_sorted import return_note_matiere
from pronote import connect_pronote
from test_app import gen_test_profil
from data_bac_gen import Predict_Algo

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = ""
    password = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
      
    pronote_info = connect_pronote(username, password)
    note_elt = Predict_Algo(pronote_info)
    prono = {'Philosophie' : note_elt.Philosophie_gen(), 'Spe1' : note_elt.Specialité_gen('Mathématiques')}

    return render_template('panel.html', pronote_info=pronote_info, note_list=return_note_matiere(pronote_info), prono=prono)
      
@app.route('/test_app', methods=['GET'])
def test_app():
    pronote_info_test = gen_test_profil()
    note_elt = Predict_Algo(pronote_info_test)
    prono = {'Philosophie' : note_elt.Philosophie_gen(), 'Spe1' : note_elt.Specialité_gen('Mathématiques')}   
    # Redirect to the panel with test data
    return render_template('panel.html', pronote_info=pronote_info_test, note_list=return_note_matiere(pronote_info_test), prono=prono)



@app.route('/preview', methods=['POST'])
def preview():
    return render_template('preview.html')

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug=True)