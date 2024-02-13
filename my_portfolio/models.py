from django.db import models

class ContactModel(models.Model):
    ism = models.CharField(null=True, blank=False, max_length=30, verbose_name='Ism')
    email = models.EmailField(null=True, blank=False,verbose_name='Email')
    nomer = models.CharField(max_length=13,null=True, blank=True,verbose_name='Nomer')
    xabar = models.TextField(null=True, blank=False, verbose_name='Xabar')

    def __str__(self):
        return f"{self.ism} - {self.nomer}"
    
    class Meta:
        verbose_name = "Kontakt ma'lumoti"
        verbose_name_plural = "Kontakt ma'lumotlari"






# # API uchun 

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name = "Post ma'lumoti "
#         verbose_name_plural = "Post ma'lumotlari "


# # class UserModel(models.Model):
# #     username = models.CharField(max_length=30, verbose_name='Username')
# #     f_name = models.CharField(max_length=30, verbose_name='Ism')
# #     l_name = models.CharField(max_length=30, verbose_name='Ism')
# #     email = models.EmailField(verbose_name='Email')
# #     age = models.DecimalField(verbose_name='Yosh')