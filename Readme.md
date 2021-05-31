Za pokretanje je potrebno imati instaliran Python3 i importan Flask module.
Projekt se pokreće naredbom 
python backend.py 

Primjer pokrenutog programa:

 * Serving Flask app 'backend' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)


 Nakon pokretanja u browseru otvoriti http://127.0.0.1:8080/

 Program dohvaća podatke iz movieList.json datoteke i servira ih browseru na putanji http://127.0.0.1:8080/movies

 Primjer:

 [{"name": "Analyze This", "year": 1999, "genre": "Comedy", "rating": "6.7/10"}, {"name": "American History X", "year": 1998, "genre": "Crime", "rating": "8.5/10"}, {"name": "Chasing Amy", "year": 1997, "genre": "Drama", "rating": "7.2/10"}, {"name": "Don't Breathe", "year": 2016, "genre": "Horror", "rating": "7.1/10"}, {"name": "Interstellar", "year": 2014, "genre": "Sci-Fi", "rating": "8.6/10"}]

 Browser pomoću javascripta dohvaća json podatke sa servera i prikazuje ih kao HTML kad se klikne na gumb "Dohvati filmove"