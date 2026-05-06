[app]

# (str) Title of your application
title = Губошлёпка

# (str) Package name
package.name = guboshlepka

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test
version = 0.1
# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,wav,ttf

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,plyer

# (str) Supported architectures (armeabi-v7a, arm64-v8a, x86, x86_64)
android.arch = armeabi-v7a, arm64-v8a

# (list) Permissions
android.permissions = VIBRATE

# (bool) Indicate if the application must be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use `--debug` flag to build
android.debug = True

# (bool) Accept SDK license
android.accept_sdk_license = True

# (str) Path to Android SDK (set by our workflow)
android.sdk_path = /home/runner/android-sdk

# (str) Path to Android NDK
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653
