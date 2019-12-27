
import webbrowser
url = "https://www.youtube.com/watch?v=YfF10ow4YEo"
with open ('/home/ubuntu/WakeUpPi/backend-request-song/song.txt', 'rt') as myfile:  # Open lorem.txt for reading text
    url = myfile.read()              # Read the entire file into a string
   
controller = webbrowser.get()
controller.open(url,new=1)

print(contents)
