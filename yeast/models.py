from django.db import models


class ProductionData(models.Model):
    batch_id = models.CharField(max_length=50)
    temperature = models.FloatField()
    ph = models.FloatField()
    nutrient_level = models.FloatField()
    fermentation_time = models.FloatField()
    initial_yeast_amount = models.FloatField()
    final_yield = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.batch_id
