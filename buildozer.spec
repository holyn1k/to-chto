[app]
title = VirusApp
package.name = virusapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.permissions = INTERNET,VIBRATE
android.minapi = 21
android.api = 31
android.archs = arm64-v8a,armeabi-v7a
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1