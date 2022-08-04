from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5443798496:AAGKRFPcVQzmdvIdYXc8USC2OaiZAdQoL3g"  # Bot toekn
ADMINS = [5587212866]  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
