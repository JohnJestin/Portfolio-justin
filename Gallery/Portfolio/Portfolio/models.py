from django.db import models

from.category import Categorie
class gallery(models.Model):
    imgtitle=models.CharField(max_length=100,blank=True, null=False)
    imgdesc=models.CharField(max_length=600 ,blank =True,null=False)
    category=models.ForeignKey(Categorie,on_delete=models.CASCADE ,default=1)
    image=models.FileField(upload_to="Images/")

    @staticmethod
    def get_all_photos():
        return gallery.objects.all()

    @staticmethod
    def get_all_photos_by_category_id(categoryID):
        if categoryID:
            return gallery.objects.filter(category=categoryID)
            
        else:
            return  gallery.get_all_photos()  
             
   