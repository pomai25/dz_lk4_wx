import wx
import os


class MainWindow(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Приветствие", size=(630, 640), pos=(100, 100))
        self.initializeUI()

    def initializeUI(self):
        panel = wx.Panel(self)
        self.setUpMainWindow(panel)
        self.Show()

    def setUpMainWindow(self, panel):
        hello_label = wx.StaticText(panel, label="всем приветик!", pos=(250, 23))
        hello_font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        hello_label.SetFont(hello_font)

        image_path = r"C:\Users\valer\OneDrive\Рабочий стол\бдшка\миньон.jpg"
        if os.path.exists(image_path):
            try:
                image = wx.Image(image_path, wx.BITMAP_TYPE_ANY)
                if image.IsOk():
                    image = image.Scale(650, 650, wx.IMAGE_QUALITY_HIGH)
                    bitmap = wx.Bitmap(image)
                    image_bitmap = wx.StaticBitmap(panel, bitmap=bitmap, pos=(0, 40))
            except Exception as e:
                print(f"Ошибка при загрузке изображения: {e}")
        else:
            print(f"Файл {image_path} не найден")


class ProfileWindow(wx.Frame):
    def __init__(self):
        super().__init__(None, title="профиль пользователя", size=(1000, 1000), pos=(550, 100))
        self.initializeUI()

    def initializeUI(self):
        panel = wx.Panel(self)
        self.setUpMainWindow(panel)
        self.Show()

    def createImageLabels(self, panel):
        image_path = r"C:\Users\valer\OneDrive\Рабочий стол\бдшка\яя.jpg"
        if os.path.exists(image_path):
            try:
                image = wx.Image(image_path, wx.BITMAP_TYPE_ANY)
                if image.IsOk():
                    image = image.Scale(500, 660, wx.IMAGE_QUALITY_HIGH)
                    bitmap = wx.Bitmap(image)
                    image_bitmap = wx.StaticBitmap(panel, bitmap=bitmap, pos=(0, 40))
            except Exception as e:
                print(f"Ошибка при загрузке изображения: {e}")
        else:
            print(f"Файл {image_path} не найден")

    def setUpMainWindow(self, panel):
        self.createImageLabels(panel)

        user_label = wx.StaticText(panel, label="Чулкова Валерия", pos=(300, 60))
        user_font = wx.Font(28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        user_label.SetFont(user_font)

        bio_label = wx.StaticText(panel, label="Биография", pos=(40, 400))
        bio_font = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        bio_label.SetFont(bio_font)

        about_label = wx.StaticText(panel, label="Студентка 2 курса МАИ, М3О-236БВ-24", pos=(40, 435))
        about_font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        about_label.SetFont(about_font)

        skills_label = wx.StaticText(panel, label="Навыки", pos=(40, 490))
        skills_font = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        skills_label.SetFont(skills_font)

        languages_label = wx.StaticText(panel, label="в процессе получения", pos=(40, 525))
        languages_font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        languages_label.SetFont(languages_font)

        experience_label = wx.StaticText(panel, label="Опыт", pos=(40, 550))
        experience_font = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        experience_label.SetFont(experience_font)

        developer_label = wx.StaticText(panel, label="web дизайн", pos=(40, 585))
        developer_font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        developer_label.SetFont(developer_font)

        dev_dates_label = wx.StaticText(panel, label="февраль 24 - май 24", pos=(40, 610))
        dev_dates_font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        dev_dates_label.SetFont(dev_dates_font)


class MyApp(wx.App):
    def OnInit(self):
        main_window = MainWindow()
        profile_window = ProfileWindow()
        return True


if __name__ == "__main__":
    app = MyApp()

    app.MainLoop()
