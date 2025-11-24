import pickle
users = {
    "Смирнов": {
        "Facebook": "Password123",
        "Google": "MyGooglePass",
        "Twitter": "TwitPass",
        "Instagram": "Insta2023",
        "VK": "Vkontakte1",
        "GitHub": "DevCode2023"
    },
    "Кузнецов": {
        "Facebook": "Fb2023!",
        "Google": "Google456",
        "Twitter": "TwitterPass",
        "Instagram": "InstaGram",
        "VK": "Vk123456",
        "GitHub": "GitHubCode"
    },
    "Попов": {
        "Facebook": "PopovFb",
        "Google": "PopovGoo",
        "Twitter": "PopovTw",
        "Instagram": "PopovInst",
        "VK": "PopovVk",
        "GitHub": "PopovGit"
    },
    "Васильев": {
        "Facebook": "VasPass1",
        "Google": "VasPass1",
        "Twitter": "Twit2023",
        "Instagram": "InstaPass",
        "VK": "VkPass123",
        "GitHub": "GitVas2023"
    },
    "Соколов": {
        "Facebook": "SokolFb",
        "Google": "SokolGoo",
        "Twitter": "SokolTw",
        "Instagram": "SokolInst",
        "VK": "SokolVk",
        "GitHub": "SokolGit"
    },
    "Морозов": {
        "Facebook": "MorozPass",
        "Google": "MorozPass",
        "Twitter": "MorozPass",
        "Instagram": "MorozPass",
        "VK": "MorozPass",
        "GitHub": "MorozPass"
    },
    "Новиков": {
        "Facebook": "NovikovFb",
        "Google": "GooglePass",
        "Twitter": "TwitNovik",
        "Instagram": "InstaNovik",
        "VK": "VkNovikov",
        "GitHub": "GitNovik"
    }
}

print("Список пользователей и средняя длина их паролей:")
for user, passwords in users.items():
    avg_len = sum(len(password) for password in passwords.values()) / len(passwords)
    print(f"{user}: {avg_len:.2f}")

print("\nСайт с самым коротким паролем у каждого пользователя:")
for user, passwords in users.items():
    min_site = min(passwords, key=lambda site: len(passwords[site]))
    print(f"{user}: {min_site} ({passwords[min_site]})")

for user, passwords in users.items():
    seen = {}
    for site, pwd in passwords.items():
        if pwd in seen.values():
            count = 1
            new_pwd = f"{pwd}_new{count}"
            while new_pwd in seen.values():
                count += 1
                new_pwd = f"{pwd}_new{count}"
            passwords[site] = new_pwd
        else:
            seen[site] = pwd
print("\nПовторяющиеся пароли заменены.\n")

fb_users = []
for user, passwords in users.items():
    fb_pass = passwords.get("Facebook", "")
    if fb_pass and fb_pass[0].isupper():
        fb_users.append(user)
print("Пользователи, у которых пароль к Facebook начинается с заглавной буквы:")
print(fb_users)

with open("data.pickle", "wb") as f:
    pickle.dump(users, f)

print("\nСловарь сохранён в data.pickle")