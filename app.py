from flask import Flask, render_template, jsonify

app = Flask(__name__)

patients = [
  {
    'id': 1,
    'first_name': 'Иван',
    'patronymic': 'Иванович',
    'last_name': 'Иванов',
    'date_of_birth': '01.01.1971'
  },
  {
    'id': 2,
    'first_name': 'Петр',
    'patronymic': 'Петрович',
    'last_name': 'Петров',
    'date_of_birth': '02.02.1972'
  },
  {
    'id': 3,
    'first_name': 'Сидор',
    'patronymic': 'Сидорович',
    'last_name': 'Сидоров',
    'date_of_birth': '03.03.1973'
  },
  {
    'id': 4,
    'first_name': 'Кузьма',
    'last_name': 'Кузнецов',
    'date_of_birth': '04.04.1974'
  },
]


@app.route('/')
def hello_world():
  return render_template('home.html', patients = patients)

@app.route('/api/patients')
def list_patients():
  return jsonify(patients)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
