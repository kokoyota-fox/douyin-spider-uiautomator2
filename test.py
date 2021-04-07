import uiautomator2 as u2
import time

if __name__ == '__main__':
    d = u2.connect_adb_wifi('192.168.1.103')
    for i in range(10):
        if d(resourceId='com.zhiliaoapp.musically:id/bse') \
                .child(resourceId='com.zhiliaoapp.musically:id/beg', index=3) \
                .child(resourceId='com.zhiliaoapp.musically:id/bs6').click_exists(5):
            if d(resourceId='com.zhiliaoapp.musically:id/apk').click_exists(5):
                time.sleep(1)
                d.press('back')