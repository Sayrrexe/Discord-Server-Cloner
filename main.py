import asyncio
import platform
import discord
from os import system, getenv, path
from dotenv import load_dotenv, set_key
from serverclone import Clone
from colorama import Fore, Style

# Инициализация переменных и окружения
load_dotenv()
TOKEN = getenv("TOKEN")
TITLE = "Discord Get - Developed by Sayrrexe"
client = discord.Client()

# Установка заголовка окна
system(f"title {TITLE}")

# Очистка консоли
OS = platform.system()
if OS == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
    


welcome_banner = f"""{Fore.GREEN}
  ______                                                                        
 /      \                                                                       
|  $$$$$$\  ______   __    __  __    __   ______    ______   __    __   ______  
| $$___\$$ |      \ |  \  |  \|  \  |  \ /      \  /      \ |  \  /  \ /      \ 
 \$$    \   \$$$$$$\| $$  | $$| $$  | $$|  $$$$$$\|  $$$$$$\ \$$\/  $$|  $$$$$$\\
 _\$$$$$$\ /      $$| $$  | $$| $$  | $$| $$   \$$| $$    $$  >$$  $$ | $$    $$ 
|  \__| $$|  $$$$$$$| $$__/ $$| $$__/ $$| $$      | $$$$$$$$ /  $$$$\ | $$$$$$$$
 \$$    $$ \$$    $$ \$$    $$ \$$    $$| $$       \$$     \|  $$ \$$\ \$$     \\
  \$$$$$$   \$$$$$$$ _\$$$$$$$ _\$$$$$$$ \$$        \$$$$$$$ \$$   \$$  \$$$$$$$
                    |  \__| $$|  \__| $$                                        
                     \$$    $$ \$$    $$                                        
                      \$$$$$$   \$$$$$$                                         
{Style.RESET_ALL}
"""

welcome_text = f"{Fore.CYAN}Добро пожаловать в Sayrrexe Discord Cloner!{Style.RESET_ALL}"

print(welcome_banner)
print(f"                                    {welcome_text}")


# Ввод данных пользователя
if not TOKEN:
    TOKEN = input(f"{Fore.YELLOW}Введите ваш Discord TOKEN: {Style.RESET_ALL}")
    # Опционально: сохранить TOKEN в .env для будущего использования
    check = input('Сохранить для будующего использованя(д\н): ')
    if check.lower() == 'д':
        env_path = path.join(path.dirname(__file__), '.env')
        if path.exists(env_path):
            set_key(env_path, "TOKEN", TOKEN)
        else:
            with open('.env', 'w') as env_file:
                env_file.write(f"TOKEN={TOKEN}\n")
input_guild_id = input('2. ID сервера, который нужно скопировать:\n >> ')
output_guild_id = input('3. ID сервера, куда нужно вставить:\n >> ')

print("\n" * 2)

# Событие: готовность бота
@client.event
async def on_ready():
    print(f"Вход выполнен: {client.user}")
    print("Клонирование началось...")

    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    if not guild_from:
        print(f"{Fore.RED}Не удалось найти сервер с ID: {input_guild_id}{Style.RESET_ALL}")
        await client.close()
        return

    if not guild_to:
        print(f"{Fore.RED}Не удалось найти сервер с ID: {output_guild_id}{Style.RESET_ALL}")
        await client.close()
        return


    # Процесс клонирования
    a = await Clone.guild_edit(guild_to, guild_from)
    if a == False:
        await client.close()
        return
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)

    # Завершающий баннер
    print(welcome_banner)

    await asyncio.sleep(5)
    await client.close()

# Запуск клиента
try:
    client.run(TOKEN, bot=False)
except discord.LoginFailure:
    print(f"{Fore.RED}Ошибка: Токен недействителен. Проверьте значение переменной 'TOKEN' в .env{Style.RESET_ALL}")
