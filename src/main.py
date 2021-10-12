import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.utils import platform
from kivy.clock import Clock
import plyer

assert platform == 'android'
from jnius import autoclass
Context = autoclass("android.content.Context")


kv = r"""
#:import plyer plyer

BoxLayout:
    orientation: 'vertical'

    Label:
        size_hint_y: None
        height: dp(50)
        text: 'Package name: %s' % app.package_name

    Label:
        size_hint_y: None
        height: dp(50)
        text: 'FILEPROVIDER_AUTHORITY:\n%s' % plyer.camera.FILEPROVIDER_AUTHORITY

    Label:
        size_hint_y: None
        height: dp(50)
        text: 'img.source:\n%s' % root.ids.img.source

    Image:
        id: img

    Button:
        size_hint_y: None
        height: dp(50)
        text: 'Take picture'
        on_release: app.take_picture()
"""

class MyApp(App):

    def init_android(self):
        self.package_name = Context.getPackageName()
        assert plyer.camera.FILEPROVIDER_AUTHORITY is None
        plyer.camera.FILEPROVIDER_AUTHORITY = f'{self.package_name}.fileprovider'

    def build(self):
        self.init_android()
        return Builder.load_string(kv)
        return self.root

    def take_picture(self):
        files_dir = Context.getExternalFilesDir('my_pics').getAbsolutePath()
        filename = files_dir + '/foo.jpg'
        print('Calling plyer.camera.take_picture', filename)
        plyer.camera.take_picture(filename, self.on_take_picture_complete)

    def on_take_picture_complete(self, filename):
        print('Picture taken!', filename)
        self.root.ids.img.source = filename
        Clock.schedule_once(lambda dt: self.root.ids.img.reload(), 0.1)

def main():
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA])
    MyApp().run()

if __name__ == '__main__':
    main()
