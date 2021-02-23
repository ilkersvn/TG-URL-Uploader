class Translation(object):
    START_TEXT = """Merhaba,
Bu bir Telegram URL Yükleme Botudur!

<b>Lütfen bana herhangi bir doğrudan indirme URL bağlantısını gönderin, Telegram'a Dosya / Video olarak yükleyebilirim</b>

/help Daha fazla ayrıntı için..

"""
    RENAME_403_ERR = "Afedersiniz. Bu dosyayı yeniden adlandırmanıza izin verilmiyor."
    ABS_TEXT = " Lütfen bencil olmayın."
    UPGRADE_TEXT = "<b>👉 Kendi Klon Botunu oluşturun..</b>  /help detaylar için"
    FORMAT_SELECTION = "İstenen formatı seçin: <a href='{}'>dosya boyutu yaklaşık olabilir</a> \nÖzel küçük resim ayarlamak istiyorsanız, aşağıdaki düğmelerden herhangi birine dokunmadan önce veya hızlıca fotoğraf gönderin.\nOtomatik oluşturulan küçük resmi silmek için /deletethumbnail 'i kullanabilirsiniz."
    SET_CUSTOM_USERNAME_PASSWORD = """Premium videoları indirmek istiyorsanız, aşağıdaki biçimi sağlayın:
URL | dosya adı | kullanıcı adı | parola"""
    NOYES_URL = "@robot URL'si algılandı. Lütfen https://shrtz.me/PtsVnf6 kullanın ve bana hızlı bir URL alın, böylece diğer kullanıcılar için yavaşlamadan Telegram'a yükleyebilirim."
    DOWNLOAD_START = "indirmeye çalışıyorum"
    UPLOAD_START = "yüklemeye çalışıyorum"
    RCHD_BOT_API_LIMIT = "izin verilen maksimum boyuttan (50MB) daha büyük boyut. Yine de, yüklemeye çalışıyorum."
    RCHD_TG_API_LIMIT = " {} saniyede indirildi.\nAlgılanan Dosya Boyutu: {}\nÜzgünüm. Ancak, Telegram API sınırlamaları nedeniyle 2GB'tan büyük dosyaları yükleyemiyorum."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Beni yararlı bulursanız lütfen bana oy verin."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = " {} saniyede indirildi. \n \n {} saniyede yüklendi."
    NOT_AUTH_USER_TEXT = "Lütfen aboneliğinizi yükseltin. /upgrade "
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Algılanan Dosya Boyutu: {}. Ücretsiz Kullanıcılar yalnızca şunları yükleyebilir: {}\nLütfen aboneliğinizi yükseltin. /upgrade \nEğer bu bir hata olduğunu düşünüyorsanız, lütfen bizimle irtibata geçin <a href='https://telegram.dog/ThankTelegram'></a>"
    SAVED_CUSTOM_THUMB_NAIL = "Özel video / dosya küçük resmi kaydedildi. Bu görüntü videoda / dosyada kullanılacaktır."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Özel küçük resim başarıyla temizlendi."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Medya başarıyla temizlendi."
    SAVED_RECVD_DOC_FILE = "Belge Başarıyla İndirildi."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Özel bir küçük resim bulunamadı."
    NO_VOID_FORMAT_FOUND = "Hata...\n<b>YouTubeDL</b> Söyledi: {}"
    USER_ADDED_TO_DB = "Kullanıcı <a href='tg://user?id={}'>{}</a> eklendi {} kadar {}."
    CURENT_PLAN_DETAILS = """Mevcut plan detayları
--------
Telegram ID: <code>{}</code>
Plan adı: Ücretsiz Klonlanmış Kullanıcı
Tarihinde sona eriyor: 31/12/2020"""
    HELP_USER = """Merhaba ben URL Yükleyici bot..
    
1. Url gönder (Link|New Name with Extension).
2. Özel Küçük Resim Gönder (İsteğe Bağlı).
3. Düğmeyi seçin.
   SVideo - Ekran Görüntüleriyle Dosyayı Video Olarak Ver
   DFile  - Ekran Görüntüleriyle Dosya Ver
   Video  - Ekran Görüntüsü Olmadan Dosyayı Video Olarak Ver
   DFile  - Ekran Görüntüsü Olmadan Dosya Ver
   
<b>👉 İletişim için </b> 👉 <a href="">Mesaj</a>

--------
Mevcut plan ayrıntılarını öğrenmek için /me yaz gönder"""
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\n© @AnyDLBot"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
