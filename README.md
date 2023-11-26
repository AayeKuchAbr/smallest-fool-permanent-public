# smallest-fool-permanent

This is an MCQ generator using OpenAI's LLMs (GPT4V as of 26/11/23), written entirely in python. It uses the "OpenAI" python library to retrieve info from the model, along with other libraries to help generate the prompt (Pillow, python-pptx, PyPDF, base64, os). Be sure to ```pip install``` the relevant libraries before use.

Also be sure to run this program in a virtual environment. At first, I didn't know how to do that, but if you're on a mac, use this as a template this this into your terminal, once you've gotten to your desired porject folder:

``` python<version> -m venv <virtual-environment-name> ```

for example, once I got to my desired folder using the ```cd``` command, I wrote:

```python3.8 -m venv MCQvenv```

I was running into a couple issues with installing all the packages on later versions of Python, but Python 3.8 should work.

Have fun with the code, and see if it helps you study. You will need an OpenAI account, which is free to register for, but you will need to add at least 10 USD to the account to have access to GPT4V. Once you generate the API key on the OpenAI website, paste it into the ```apikey``` variable in ```callOpenAI.py```.  

xoxo, gossip girl.

PS: I'm not a particularly skilled programmer, so if there are any glaring fixes, be sure to issue a pull request, and I'll try to take a look at them.

