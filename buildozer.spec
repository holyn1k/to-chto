[app]

title = Моя Школа
package.name = moyashkola
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
osx.kivy_version = 2.2.1
fullscreen = 1

android.permissions = INTERNET
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.api = 31

# Используй кириллицу в интерфейсе
android.allow_unicode = 1

# Язык по умолчанию
android.manifest_placeholders = appLabel="Моя Школа"

# Где лежат иконки и сплеш-экраны (можно убрать, если не используешь)
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/splash.png

[buildozer]

log_level = 2
warn_on_root = 0
