[app]

title = Plyer Camera Example
package.name = camera_example
package.domain = eu.antocuni

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 0.1

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know
# what you're doing
# android.numeric_version = 1

requirements = python3,
               kivy==2.0.0,
               pillow==7.0.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
#android.api = 27
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

android.arch = armeabi-v7a


# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# use my fork and branch of of python-for-android:
#     https://github.com/antocuni/python-for-android/tree/fileprovider-rebased
# which contains an up-to-date and rebased version of this PR:
#     https://github.com/kivy/python-for-android/pull/1922
p4a.fork = antocuni
p4a.branch = fileprovider-rebased


# NOTE: to use the option p4a.extra_args you need this buildozer branch:
#     https://github.com/antocuni/buildozer/tree/antocuni/p4a-extra-args
# see also env.buildozer_version in .github/workflows/buildozer.yml
#
# add a fileprovider
p4a.extra_args = --fileprovider-paths=/github/workspace/src/file_paths.xml



[buildozer]
log_level = 2

