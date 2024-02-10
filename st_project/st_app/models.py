from django.db import models

class TeamA(models.Model):
    id = models.AutoField(primary_key=True)
    time=models.TimeField(max_length=10,unique=True)
    shot=models.CharField(max_length=50,null=False)
    made=models.CharField(max_length=50,null=True)
    made_SJN=models.CharField(max_length=50,null=True)
    made_locx=models.FloatField(max_length=50,null=True)
    made_locy=models.FloatField(max_length=50,null=True)
    made_assist=models.CharField(max_length=50,null=True)
    made_shottype=models.CharField(max_length=50,null=True)
    miss=models.CharField(max_length=50,null=True)
    miss_outb=models.CharField(max_length=50,null=True)
    miss_reb=models.CharField(max_length=50,null=True)
    o_reb_SJN=models.CharField(max_length=50,null=True)
    d_reb_DJN=models.CharField(max_length=50,null=True)
    shot_foul=models.CharField(max_length=50,null=True)
    shot_foul_SJN=models.CharField(max_length=50,null=True)
    shot_foul_Slocx=models.FloatField(max_length=50,null=True)
    shot_foul_Slocx=models.FloatField(max_length=50,null=True)
    shot_foul_DJN=models.CharField(max_length=50,null=True)
    shot_foul_Dlocx=models.FloatField(max_length=50,null=True)
    shot_foul_Dlocx=models.FloatField(max_length=50,null=True)
    mwf=models.CharField(max_length=50,null=True)
    mwf_SJN=models.CharField(max_length=50,null=True)
    mwf_Slocx=models.FloatField(max_length=50,null=True)
    mwf_Slocy=models.FloatField(max_length=50,null=True)
    mwf_assist=models.CharField(max_length=50,null=True)
    mwf_shottype=models.CharField(max_length=50,null=True)
    mwf_DJN=models.CharField(max_length=50,null=True)
    mwf_Dlocx=models.FloatField(max_length=50,null=True)
    mwf_Dlocy=models.FloatField(max_length=50,null=True)

    
def __init__(self):
   return self.id
   
