from django.db import models
from django.contrib.auth import get_user_model

class Favorite(models.Model):
  state = models.CharField(max_length=2)
  ecoregion = models.CharField(max_length=50)
  type = models.CharField(max_length=50)
  common_name = models.CharField(max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    return f"The {self.ecoregion} is in {self.state}. {self.common_name} is a {self.type}"

  def as_dict(self):
    return {
      'id': self.id,
      'state': self.state,
      'ecoregion': self.ecoregion,
      'type': self.type,
      'common_name': self.common_name
    }
