from django.db import models

class Category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.category_name


class CarMake(models.Model):
    car_make_name=models.CharField(max_length=100)

    def __str__(self):
        return self.car_make_name

class CarModel(models.Model):
    model_name=models.CharField(max_length=50)

    def __str__(self):
        return self.model_name


class Car(models.Model):
    car_name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    car_make=models.ForeignKey(CarMake,on_delete=models.CASCADE)
    model=models.ForeignKey(CarModel,on_delete=models.CASCADE)
    description=models.TextField()
    year=models.IntegerField(default=0)
    price=models.DecimalField(verbose_name='cost',max_digits=10,decimal_places=3)
    add_date=models.DateTimeField(verbose_name='date',auto_now_add=True)
    city=models.CharField(verbose_name='city',max_length=50)
    country=models.CharField(verbose_name='country', max_length=50)
    mileage=models.IntegerField(default=0)
    with_photo=models.BooleanField(default=True,null=True,blank=True)


    CHOICES_DRIVE=(
        ('задный','задный'),
        ('передний', 'передний'),
        ('полны',  'полны')
    )
    drive = models.CharField(verbose_name='Привод', max_length=16, choices=CHOICES_DRIVE)

    CHOICES_ENGINE=(
        ('бензин','бензин'),
        ('газ','газ') ,
        ('дизель','дизель') ,
        ('электрический', 'электрический')
    )
    engine = models.CharField(max_length=16, choices=CHOICES_ENGINE)
    volume=models.FloatField(default=0.8)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):                        
        return self.car_name                  

