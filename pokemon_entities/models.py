from django.db import models



class Pokemon(models.Model):
    title = models.CharField('Имя покемона',max_length=100)
    title_en = models.CharField('Имя на англ',max_length=100)
    title_jp = models.CharField('Имя на японском',max_length=100)
    image = models.ImageField('Изображение',blank=True, null=True)
    description = models.TextField('Описание',max_length=500,blank=True, null=True)
    previous_evolution = models.ForeignKey('self',verbose_name='Эволюционировал из' ,on_delete=models.SET_NULL,null=True, related_name='next_evolution')


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entities',verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Появился')
    disappeared_at = models.DateTimeField(verbose_name='Исчез')
    level = models.IntegerField(blank=True, null=True,verbose_name='Уровень')
    health = models.IntegerField(blank=True, null=True,verbose_name='Здоровье')
    strength = models.IntegerField(blank=True, null=True,verbose_name='Сила')
    defense = models.IntegerField(blank=True, null=True,verbose_name='Защита')
    stamina = models.IntegerField(blank=True, null=True,verbose_name='Выносливость')