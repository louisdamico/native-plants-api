from django.db import models
from django.contrib.auth import get_user_model

class Favorite(models.Model):
  list_name = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  ecoregion = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  common_name = models.CharField(max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    return f"The List:{self.list_name}, {self.ecoregion} is in {self.state}. {self.common_name} is a {self.type}"

  def as_dict(self):
    return {
      'id': self.id,
      'list_name': self.list_name,
      'state': self.state,
      'ecoregion': self.ecoregion,
      'type': self.type,
      'common_name': self.common_name
    }
