import uiautomator2 as u2
import time
import asyncio


class Douyin:

    def __init__(self, config):
        self.connect = u2.connect_adb_wifi(config['ip'])
        self.size = self.__get_windows_size()
        self.count = config['count'].values[0]
        self.config = config
        self.__handler_watch()
        self.already = []

    '''监听错误'''

    def __handler_watch(self):
        # self.connect.watcher().when()
        pass

    def __start_app(self):
        """启动app"""
        self.connect.app_start(package_name='com.zhiliaoapp.musically')

    def __get_windows_size(self):
        """获取手机尺寸大小"""
        return self.connect.window_size()

    def __handler_up(self):
        x1 = int(self.size[0] * 0.7)
        y1 = int(self.size[1] * 0.75)
        y2 = int(self.size[1] * 0.25)
        self.connect.swipe(x1, y1, x1, y2, duration=0.05)

    def select_into__direct_broadcasting_room_scribe(self, start=True):
        if start:
            self.__start_app()
            self.connect(text='收件匣').click_exists(5)
            self.connect(resourceId='com.zhiliaoapp.musically:id/bzi', text='觀看').click_exists(5)
        size = self.count
        while size > 0:
            self.__direct_broadcasting_stream_user_scribe()
            self.connect.press('back')
            size = size - 1

    def random_direct_broadcasting_room_scribe(self, start=True):
        """ 直播间的关注"""
        # 等待某个activity10秒，如果找到了就直接启动
        # if self.connect.wait_activity('', timeout=10) :
        if start:
            self.__start_app()
            while True:
                self.__handler_up()
                time.sleep(1)
                if self.connect(text='直播').exists:
                    break
            '''点击直播间'''
            self.connect(text='直播').click_exists(5)
        size = self.count
        while size > 0:
            self.__direct_broadcasting_stream_user_scribe()
            '''返回'''
            self.connect.press('back')
            size = size - 1

    def __direct_broadcasting_stream_user_scribe(self):
        """点击进来的用户"""
        self.connect.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/bse"]/android.view.ViewGroup['
                           '4]/android.widget.ImageView[1]') \
            .click_exists(5)
        time.sleep(1)
        '''这个直播间没啥人，换一个直播间'''
        if self.connect(resourceId='com.zhiliaoapp.musically:id/aq5', text='關注中').exists or \
                self.connect(resourceId='com.zhiliaoapp.musically:id/dax', text='直播已結束').exists:
            self.connect.press('back')
            self.__handler_up()
            self.random_direct_broadcasting_room_scribe(start=False)
            return
        '''点击关注'''
        if self.connect(resourceId='com.zhiliaoapp.musically:id/apk').click_exists(5):
            time.sleep(1)
            self.connect.press('back')

    async def fans_list_scribe_and_personal_letter(self, start=True):
        """粉丝列表关注和私信"""
        if start:
            self.__start_app()
        self.connect(resourceId='com.zhiliaoapp.musically:id/br3').click_exists(5)
        self.connect(resourceId='com.zhiliaoapp.musically:id/aq_') \
            .child(resourceId='com.zhiliaoapp.musically:id/aq8', text='粉丝').click_exists(5)
        task = [
            self.personal_letter()
        ]
        await asyncio.gather(*task)

    async def personal_letter(self):
        """私信"""
        users = self.connect(resourceId='com.zhiliaoapp.musically:id/cj6').child(
            resourceId='com.zhiliaoapp.musically:id/dqg')
        for user in users:
            if user.info['text'] in self.already:
                continue
            self.already.append(user.info['text'])
            user.click_exists(5)
            self.connect(resourceId='com.zhiliaoapp.musically:id/co5', text='訊息').click_exists(2)
            response = self.config['1']
            self.connect(resourceId='com.zhiliaoapp.musically:id/bue').set_text(response)
            self.connect(resourceId='com.zhiliaoapp.musically:id/cnw').click_exists(2)
            response = self.config['2']
            self.connect(resourceId='com.zhiliaoapp.musically:id/bue').set_text(response)
            self.connect(resourceId='com.zhiliaoapp.musically:id/cnw').click_exists(2)
            response = self.config['3']
            self.connect(resourceId='com.zhiliaoapp.musically:id/bue').set_text(response)
            self.connect(resourceId='com.zhiliaoapp.musically:id/cnw').click_exists(2)
            response = self.config['mobile']
            self.connect(resourceId='com.zhiliaoapp.musically:id/bue').set_text(str(response))
            self.connect(resourceId='com.zhiliaoapp.musically:id/cnw').click_exists(2)
            time.sleep(1)
            self.connect.press('back')
            time.sleep(1)
            self.connect.press('back')
            time.sleep(1)
        all_users = [i.info['text'] for i in users]
        if set(all_users).issubset(set(self.already)):
            return
        self.__handler_up()
        self.__handler_up()
        task = [
            self.personal_letter()
        ]
        await asyncio.gather(*task)
