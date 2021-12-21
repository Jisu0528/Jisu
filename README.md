# Term Project

>## 이미지에서 텍스를 인지해서 음성으로 출력
>
>>20101309 한지수
>
>
>
>### 이미지를 텍스트 파일로 변환
>
>> ```python
>> from PIL import Image
>> import pytesseract
>> 
>> pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
>> 
>> image = Image.open("test2.jpg")
>> result = pytesseract.image_to_string(image)
>> 
>> print(result)
>> 
>> with open("text.txt", "w", encoding="utf8") as x:
>>     x.write(result)
>>     x.write("\n\n\n")
>>     x.write(result)
>> ```
>>
>> pytesseract를 이용해 이미지 속의 텍스트를 추출해 text.txt 파일로 저장한다.
>
>
>
>>### 텍스트 파일을 음성으로 읽기
>>
>>```python
>>from gtts import gTTS
>>import playsound
>>
>>txtfile = "text.txt"
>>y = open(txtfile, 'r', encoding='utf8')
>>text = y.read()
>>
>>def speak(text) :
>>    tts = gTTS(text=text)
>>    soundfile='voice.mp3'
>>    tts.save(soundfile)
>>    playsound.playsound(soundfile)
>>    
>>speak(text)
>>```
>>
>>텍스트 파일을 읽고 음성으로 추출한다.
>
>
>
>> ### 실행 결과
>>
>> #### 이미지 파일
>>
>> ![](C:\Users\01052\Desktop\대학\2-2\오픈소스\test2.JPG)
>>
>> BBC 기사 일부 발취(<https://www.bbc.com/news/world-africa-59697807>)
>>
>> 
>>
>> #### 텍스트 파일
>>
>> ![image-20211221234217357](C:\Users\01052\AppData\Roaming\Typora\typora-user-images\image-20211221234217357.png)
>>
>> 
>>
>> #### 음성 파일
>>
>> <audio src="C:\Users\01052\Desktop\대학\2-2\오픈소스\voice.mp3"></audio>

> #### 참고한 사이트
>
> https://www.delftstack.com/ko/howto/python/python-text-to-speech/
>
> https://niceman.tistory.com/157
