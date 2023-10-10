import openai

openai.api_key = open("key.txt", "r").read().strip("\n")

response = openai.Image.create_variation(
  image=open("img/hpa.png", "rb"),
  n=3,
  size="512x512"
)
image_url = response['data'][0]['url']
print(image_url)
image_url = response['data'][1]['url']
print(image_url)
image_url = response['data'][2]['url']
print(image_url)
