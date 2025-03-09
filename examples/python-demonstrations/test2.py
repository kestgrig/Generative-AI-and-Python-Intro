# Importuojama requests biblioteka, kad galėtume siųsti HTTP užklausas
import requests 

# def nurodo kad define funkcija su pavadinimu 
# get_jsonplaceholder_data ir ji paima parametrus endpoint="posts/1" 
# kuriu default reiksme yra string
# Funkcijos apibrėžimas. Funkcija gauna vieną parametrą "endpoint", 
# kurio numatytoji reikšmė yra "posts/1"

def get_jsonplaceholder_data(endpoint="posts/1"):
# Sukuriame URL, kuriuo atliksime užklausą. "f" reikšmė naudojama f-string sintaksei.
# Šis URL naudoja "endpoint" parametrą, kad nurodytų, kokius duomenis gauti.
    url = f"https://jsonplaceholder.typicode.com/{endpoint}"

# Atliekame GET užklausą į sukurtą URL 
    response = requests.get(url)

# Patikriname, ar užklausa pavyko (statuso kodas 200 - OK)
    if response.status_code == 200:

# Jei atsakymo statusas yra 200, tai grąžiname atsakymo duomenis kaip JSON
        return response.json()

# Jei atsakymo statusas nėra 200 (t.y. užklausa nepavyko), grąžiname klaidos žinutę
    else:
        return {"error": f"Failed to fetch data. Status code: {response.status_code}"}

# Funkcijos iškvietimas su numatyta reikšme "posts/1"
data = get_jsonplaceholder_data()
# Atspausdiname gautus duomenis arba klaidos pranešimą
print(data)

