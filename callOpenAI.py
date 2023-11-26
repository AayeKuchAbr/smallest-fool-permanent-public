import openai
import os
import base64

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


def call(text, lecture_name):
    testcase = "say hi"
    keyname = "zoinks" #edit with your openai API key
    openai.api_key = keyname

    image_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lecture_images")

    #define content


    content = []

    content.append({"type":"text", "text": text})
    for image in os.listdir(image_directory):
        base64_image = encode_image(os.path.join(image_directory, image))
        content.append({"type":"image_url", "image_url":{"url":f"data:image/png;base64,{base64_image}","detail":"low"}})
    message = {"role": "user", "content": content}
    
    response = openai.ChatCompletion.create(model="gpt-4-vision-preview",messages=[message],temperature = 0.7, max_tokens = 4096)
    

    try:
        if lecture_name[-3:]=="pdf":
            output_file = f"{lecture_name[:-4]} questions.txt"
        else:
            output_file = f"{lecture_name[:-5]} questions.txt"


        script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"lecture questions")

        
        output_file_path = os.path.join(script_dir, output_file)
            
        with open(output_file_path, "w") as file:

            file.write(response["choices"][0]["message"]["content"])


        print(f"API response saved to {output_file}")
    except AssertionError:
            
        print(f"Failed to retrieve data. Status code: {response.status_code}")



