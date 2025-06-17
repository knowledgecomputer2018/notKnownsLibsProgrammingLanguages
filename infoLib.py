#کد تبدیل ویدیو به متن از طریق ماتریس تصویری + OCR (Tesseract):
#import cv2
import opencv
import pytesseract

# آدرس ویدیو
video_path = 'input_video.mp4'
cap = cv2.VideoCapture(video_path)

#تبدیل به یک صفحه ی اچ تی ام ال برای مشاهده
print(cv2.getBuildInformation())