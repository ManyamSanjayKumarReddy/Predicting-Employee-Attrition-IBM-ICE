import requests

url = "https://instagram-data12.p.rapidapi.com/search/"

querystring = {"query":"insta"}

headers = {
	"X-RapidAPI-Key": "75296dc20dmsh63fba10cd8681dcp1f0aeajsn2df4b6ad72c9",
	"X-RapidAPI-Host": "instagram-data12.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response)

print(response.text)