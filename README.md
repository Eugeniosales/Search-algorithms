# Classical Search Algorithms Comparator

This project aims to compare the accuracy of the methods, relying on the number steps and time to find the desired value, serving it in a Web app with Flask and Chart.js API to show the results.

## Open With
* https://comparador-metodos-busca.herokuapp.com/


## Execute locally with Virtual
* Create the virtualenv: `virtualenv -p python3 env`
* Activate with: `source env/bin/activate`
* Install the requirements: `pip install -r requirements.txt`
* Run the Web Server: `gunicorn app:app --bind 0.0.0.0:5000 --reload`

## Workflow
1) Put the max value of the array
2) Define the value that will be searched
3) Choose 2 algorithms to be compared
4) See the results in the bar chart