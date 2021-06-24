from django.db import models


class ObjectActs (models.Model):
    create_date = models.DateField(blank=False, auto_now_add=True)
    address = models.CharField(max_length=500, verbose_name='Адрес', blank=False)
    work = models.CharField(max_length=500, verbose_name='Работа')
    client = models.CharField(max_length=500, verbose_name='Заказчик с реквизитами')
    designer = models.CharField(max_length=500, verbose_name='Проектант с реквизитами')
    contractor = models.CharField(max_length=500, verbose_name='Подрядчик с реквизитами')
    supervisor_engineer = models.CharField(max_length=200, verbose_name='Технадзор')
# TODO Выяснить длину поля технадзора
    contractor_engineer = models.CharField(max_length=200, verbose_name='Прораб')
# TODO Выяснить длину поля прораба
    designer_engineer = models.CharField(max_length=200, verbose_name='Проектировщик', blank=True)
# TODO Выяснить длину поля проектировщика
    project_number = models.CharField(max_length=100, verbose_name='Ном. проекта')
    exec_documents = models.CharField(max_length=500, verbose_name='Исполн.')
    supervisor_engineer_decree = models.CharField(max_length=200, verbose_name='Приказ технадзора')
    contractor_engineer_decree = models.CharField(max_length=200, verbose_name='Приказ прораба')
    designer_engineer_decree = models.CharField(max_length=200, verbose_name='Приказ проектировщика', blank=True)
    acts_instance_num = models.CharField(max_length=100, verbose_name='Кол-во экземпляров', blank=True)

    class Meta:
        verbose_name = 'Набор актов объекта '
        verbose_name_plural = 'Наборы актов объекта'

    def __str__(self):
        return f'{self.work} -> {self.address}'

    class AOSR(models.Model):
        act_number = models.CharField(max_length=20, verbose_name='Ном. Акта', blank=True)
        act_date = models.CharField(max_length=50, verbose_name='Дата Акта')
        presented_work = models.CharField(max_length=500, verbose_name='Предъявл.')
        materials = models.CharField(max_length=500, verbose_name='Материалы')
        permitted_work = models.CharField(max_length=500, verbose_name='Разрешено')
        begin_date = models.CharField(max_length=50, verbose_name='От:')
        end_date = models.CharField(max_length=50, verbose_name='До:')
        work_SNIP = models.CharField(max_length=500, verbose_name='СНИП:', blank=True)
        docs = models.CharField(max_length=500, verbose_name='Предьявлены документы',
                                default='исполнительная схема, сертификаты/свителельства', blank=True)
        annex = models.CharField(max_length=500, verbose_name='Приложения', blank=True)

        object_acts = models.ForeignKey('ObjectActs', on_delete=models.CASCADE, verbose_name='Набор актов объекта',
                                        related_name='aosr_set')

        class Meta:
            verbose_name = 'Акт скрытых'
            verbose_name_plural = 'Акты скрытых'

        def __str__(self):
            return f'{self.act_number} -> {self.presented_work}'

    class AOSRFile(models.Model):
        file_name = models.FileField(upload_to='/media/%Y/%m/%d/', verbose_name='Файл к акту')
        description = models.CharField(max_length=255, verbose_name='Описание')
        corner_text = models.CharField(max_length=255,verbose_name='Текст в углу', blank=True)
        aosr = models.ForeignKey('AOSR', on_delete=models.CASCADE, verbose_name='файлы',
                                 related_name='files')

        class Meta:
            verbose_name = 'Файл к АОСР'
            verbose_name_plural = 'Файлы для АОСР'

        def __str__(self):
            return f'Файл {self.description}'
