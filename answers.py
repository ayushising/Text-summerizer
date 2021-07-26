import wikipedia
import re


def summary(data):
    data=wikipedia.page(data)
    text=data.content
    # removing Urls from the text
    text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', ' ', text)
       
    # removing emojis from the text
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    
    text=emoji_pattern.sub(r' ', text)
    #remove special characters
    text=re.sub(r"[-()\"#/@;:<>{}`+=~|!?,]", " ", text)
    
    #removing multiple empty line
    text=re.sub(r'[\r\n][\r\n]{2,}', '\n\n', text)
    
    return text

print(summary("Hackers"))