import srt
from deep_translator import GoogleTranslator
from tqdm import tqdm

# 載入 SRT 檔案
srt_file_path = "week11_part3.srt"
with open(srt_file_path, "r", encoding="utf-8") as file:
    srt_content = file.read()

# 解析 SRT 內容
subtitles = list(srt.parse(srt_content))

# 初始化翻譯器
translator = GoogleTranslator(source='auto', target='en')

# 翻譯每個字幕的內容並顯示進度條
for subtitle in tqdm(subtitles, desc="Translating subtitles"):
    translated_text = translator.translate(subtitle.content)
    subtitle.content = translated_text

# 將字幕轉回 SRT 格式
translated_srt_content = srt.compose(subtitles)

# 儲存翻譯後的 SRT 內容到新檔案
translated_srt_file_path = "week11_part3_translated.srt"
with open(translated_srt_file_path, "w", encoding="utf-8") as translated_file:
    translated_file.write(translated_srt_content)

print(f"翻譯完成！已將結果儲存到 {translated_srt_file_path}")
