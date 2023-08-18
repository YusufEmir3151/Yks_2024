from datetime import datetime
import time
from os import system

# İstediğiniz tarihi belirtin
target_date = datetime(2024, 6, 22, 10, 0, 0)

while True:
    # Şu anki tarihi alın
    current_date = datetime.now()

    # İstediğiniz tarih ile şu anki tarih arasındaki farkı hesaplayın
    time_left = target_date - current_date

    # Gün, saat ve dakika cinsinden süreyi alın
    days_left = time_left.days
    hours_left, remainder = divmod(time_left.seconds, 3600)
    minutes_left, seconds_left = divmod(remainder, 60)

    print(f"{days_left} gün, {hours_left} saat, {minutes_left} dakika, {seconds_left} saniye")
    system("cls")

    # Her saniye güncellemek için bekleyin
    time.sleep(0.1)
