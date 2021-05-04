def speak(str):
      from win32com.client import Dispatch
      speak=Dispatch("SAPI.SpVoice")
      speak.Speak(str)

speak("hello rajesh")
speak("import module")
speak("sir importing module")