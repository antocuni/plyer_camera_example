# plyer_camera_example

This is a kivy example app which demonstrate how to use
``plyer.camera.take_picture`` on Android API versions >= 24.

Starting with that version, you need to use a [FileProvider](https://developer.android.com/reference/androidx/core/content/FileProvider) in order to save
a picture taken with the ``ACTION_IMAGE_CAPTURE`` intent.


If you target Android API 24 (or higher) and use `plyer<=2.0.0`, when you call
`plyer.camera.take_picture` you get an error like this:

```
jnius.jnius.JavaException:` JVM exception occurred: file://foo.jpg exposed beyond app through `ClipData.Item.getUri()
```

See also [Plyer issue #500](https://github.com/kivy/plyer/issues/500).

At the moment of writing, the required functionalities are not present in the
master versions of `plyer`, `p4a` and `buildozer`, so you need a
fork of all of those.

  - `plyer` branch [antocuni/android-24-camera](https://github.com/antocuni/plyer/tree/antocuni/android-24-camera), see also PR XXX. This is also the plyer version which is vendored in this repository.
  
  - `p4a` branch [fileprovider-rebased](https://github.com/antocuni/python-for-android/tree/fileprovider-rebased), see also [PR #1922](https://github.com/kivy/python-for-android/pull/1922]).
  
  - `buildozer` branch [antocuni/p4a-extra-args](https://github.com/antocuni/buildozer/tree/antocuni/p4a-extra-args), see also PR XXX.

The key points are:

  1. in `buildozer.spec`: `p4a.extra_args = --fileprovider-paths=/github/workspace/src/file_paths.xml`: this is needed to add a FileProvider in `AndroidManifest.xml`
  
  2. in `main.py`, the following lines instruct `plyer` to use the correct
     FileProvider authority to save the image:

```python
        self.package_name = Context.getPackageName()
        assert plyer.camera.FILEPROVIDER_AUTHORITY is None
        plyer.camera.FILEPROVIDER_AUTHORITY = f'{self.package_name}.fileprovider'
```

See also `.github/workflow/buildozer.yml` for the full configuration needed to build the APK with the [buildozer action](https://github.com/ArtemSBulgakov/buildozer-action)
