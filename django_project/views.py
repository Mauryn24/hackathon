import requests
from django.shortcuts import render

def home(request):
  # Using Apis
  # define a variable to store the data
  response = requests.get(" https://api.github.com/events")
  #  grab data
  data = response.json()
  # what are you taking from API
  results = data[0]["repo"]
  
  #  render the template
  return render(request, 'templates/index.html', {'results': results})