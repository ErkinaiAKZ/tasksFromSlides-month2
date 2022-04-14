#ВВЕДЕНИЕ В ООП

class Notebook:
    def __init__(self, notebook_model, CPU, RAM, videocard, HDD, Motherboard, screensize):
        self.notebook_model = notebook_model
        self.CPU = CPU
        self.RAM = RAM
        self.videocard = videocard
        self.HDD = HDD
        self.Motherboard = Motherboard
        self.screensize= screensize

    def display_notebook(self):
        d = {
            'Модель' : self.notebook_model,
            'Процессор' : self.CPU,
            'Оперативная Память' : self.RAM,
            'Видео карта' : self.videocard,
            'Жёсткий Диск' : self.HDD,
            'Материнская плата' : self.Motherboard,
            'Размер экрана' : self.screensize
             }
        return d


macbook = Notebook(notebook_model='MacBookAir', CPU='Apple M1 8‑ядерный процессор', RAM='8 ГБ', videocard='встроенная',HDD='SSD 256 ГБ', Motherboard='A2337', screensize='13,3 дюйма')
asus = Notebook(notebook_model='ASUS ROG Zephyrus', CPU='AMD Ryzen 7 5800HS 2.8 ГГц', RAM='16 ГБ', videocard='Nvidia GeForce 3050 Ti ', HDD='SSD 512 ГБ', Motherboard='GX701GVR', screensize='14 дюйма' )
acer = Notebook(notebook_model='Acer Nitro', CPU='Intel Core i5-10300H', RAM='12 GB DDR4', videocard='NVIDIA RTX 3050', HDD='HDD 1000 GB', Motherboard='AN515', screensize='17.3 дюйма')

print(macbook.display_notebook())
print(asus.display_notebook())
print(acer.display_notebook())