# plyer_camera_example

This is a kivy example app which demonstrate how to use
``plyer.camera.take_picture`` on Android API versions >= 24.

Starting with that version, you need to use a `FileProvider` in order to save
a picture taken with the ``ACTION_IMAGE_CAPTURE`` intent.

