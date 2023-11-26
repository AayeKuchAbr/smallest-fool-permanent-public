import os
from genPrompt import prompt
from callOpenAI import call
directory=os.path.dirname(os.path.abspath(__file__))

lecture_path = os.path.join(directory,"lecture pdfs") #path for lecture pdfs to be converted


def main():
    lec_name = input("filename:\t")
    testprompt = prompt(lec_name, lecture_path)
    testprompt.get_images()
    call(testprompt.get_text(), lec_name)
    for i in os.listdir(os.path.join(directory, "lecture_images")):
        os.remove(os.path.join(os.path.join(directory,"lecture_images"), i))

main()

