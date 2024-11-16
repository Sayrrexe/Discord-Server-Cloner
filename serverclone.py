import discord
from colorama import Fore, init, Style

# Initialize colorama
init(autoreset=True)

def print_add(message):
    print(f'{Fore.GREEN}[+]{Style.RESET_ALL} {message}')

def print_delete(message):
    print(f'{Fore.BLUE}[-]{Style.RESET_ALL} {message}')

def print_warning(message):
    print(f'{Fore.RED}[WARNING]{Style.RESET_ALL} {message}')

def print_error(message):
    print(f'{Fore.RED}[ERROR]{Style.RESET_ALL} {message}')

class Clone:
    @staticmethod
    async def roles_delete(guild_to: discord.Guild):
        for role in guild_to.roles:
            if role.name != "@everyone":
                try:
                    await role.delete()
                    print_delete(f"Удалена роль: {role.name}")
                except (discord.Forbidden, discord.HTTPException) as e:
                    print_error(f"Ошибка удаления роли {role.name}: {e}")

    @staticmethod
    async def roles_create(guild_to: discord.Guild, guild_from: discord.Guild):
        roles = [role for role in guild_from.roles if role.name != "@everyone"]
        roles.reverse()
        for role in roles:
            try:
                await guild_to.create_role(
                    name=role.name,
                    permissions=role.permissions,
                    colour=role.colour,
                    hoist=role.hoist,
                    mentionable=role.mentionable
                )
                print_add(f"Создана роль: {role.name}")
            except (discord.Forbidden, discord.HTTPException) as e:
                print_error(f"Ошибка создания роли {role.name}: {e}")

    @staticmethod
    async def channels_delete(guild_to: discord.Guild):
        for channel in guild_to.channels:
            try:
                await channel.delete()
                print_delete(f"Удален канал: {channel.name}")
            except (discord.Forbidden, discord.HTTPException) as e:
                print_error(f"Ошибка удаления канала {channel.name}: {e}")

    @staticmethod
    async def categories_create(guild_to: discord.Guild, guild_from: discord.Guild):
        for channel in guild_from.categories:
            try:
                overwrites_to = {
                    discord.utils.get(guild_to.roles, name=key.name): value
                    for key, value in channel.overwrites.items()
                }
                new_channel = await guild_to.create_category(
                    name=channel.name,
                    overwrites=overwrites_to
                )
                await new_channel.edit(position=channel.position)
                print_add(f"Создана категория: {channel.name}")
            except (discord.Forbidden, discord.HTTPException) as e:
                print_error(f"Ошибка создания категории {channel.name}: {e}")

    @staticmethod
    async def channels_create(guild_to: discord.Guild, guild_from: discord.Guild):
        for channel_text in guild_from.text_channels:
            await Clone.create_text_channel(guild_to, channel_text)
        for channel_voice in guild_from.voice_channels:
            await Clone.create_voice_channel(guild_to, channel_voice)

    @staticmethod
    async def create_text_channel(guild_to: discord.Guild, channel_text: discord.TextChannel):
        try:
            category = discord.utils.get(guild_to.categories, name=getattr(channel_text.category, 'name', None))
            overwrites_to = {
                discord.utils.get(guild_to.roles, name=key.name): value
                for key, value in channel_text.overwrites.items()
            }
            new_channel = await guild_to.create_text_channel(
                name=channel_text.name,
                overwrites=overwrites_to,
                position=channel_text.position,
                topic=channel_text.topic,
                slowmode_delay=channel_text.slowmode_delay,
                nsfw=channel_text.nsfw
            )
            if category:
                await new_channel.edit(category=category)
            print_add(f"Создан текстовый канал: {channel_text.name}")
        except (discord.Forbidden, discord.HTTPException) as e:
            print_error(f"Ошибка создания текстового канала {channel_text.name}: {e}")

    @staticmethod
    async def create_voice_channel(guild_to: discord.Guild, channel_voice: discord.VoiceChannel):
        try:
            category = discord.utils.get(guild_to.categories, name=getattr(channel_voice.category, 'name', None))
            overwrites_to = {
                discord.utils.get(guild_to.roles, name=key.name): value
                for key, value in channel_voice.overwrites.items()
            }
            new_channel = await guild_to.create_voice_channel(
                name=channel_voice.name,
                overwrites=overwrites_to,
                position=channel_voice.position,
                bitrate=channel_voice.bitrate,
                user_limit=channel_voice.user_limit
            )
            if category:
                await new_channel.edit(category=category)
            print_add(f"Создан голосовой канал: {channel_voice.name}")
        except (discord.Forbidden, discord.HTTPException) as e:
            print_error(f"Ошибка создания голосового канала {channel_voice.name}: {e}")

    @staticmethod
    async def emojis_delete(guild_to: discord.Guild):
        for emoji in guild_to.emojis:
            try:
                await emoji.delete()
                print_delete(f"Удален эмодзи: {emoji.name}")
            except (discord.Forbidden, discord.HTTPException) as e:
                print_error(f"Ошибка удаления эмодзи {emoji.name}: {e}")

    @staticmethod
    async def emojis_create(guild_to: discord.Guild, guild_from: discord.Guild):
        for emoji in guild_from.emojis:
            try:
                emoji_image = await emoji.url.read()
                await guild_to.create_custom_emoji(name=emoji.name, image=emoji_image)
                print_add(f"Создан эмодзи: {emoji.name}")
            except (discord.Forbidden, discord.HTTPException) as e:
                print_error(f"Ошибка создания эмодзи {emoji.name}: {e}")

    @staticmethod
    async def guild_edit(guild_to: discord.Guild, guild_from: discord.Guild):
        try:
            try:
                icon_image = await guild_from.icon_url.read() if guild_from.icon_url else None
                await guild_to.edit(name=guild_from.name, icon=icon_image)
                print_add(f"Изменен значок сервера: {guild_to.name}")
                return True
            except:
                print_warning('Сервер не существует, или вы в нём не состоите, для начала зайдите на сервер с аккаунта, с которого производите парсинг')
                return False
        except (discord.Forbidden, discord.HTTPException) as e:
            print_error(f"Ошибка изменения значка сервера {guild_to.name}: {e}")
            return False
