from django.contrib.auth.base_user import BaseUserManager

class EduUserManager(BaseUserManager):

    """
        Creates and saves a User with given username,email and password
    """
    def create_user(self, username, password, email, first_name, last_name, usertype):
        if not username:
            raise ValueError("Users must provide username")
        if not email:
            raise ValueError("Users must provide Emails")
        
        user = self.model(username=username, email = self.normalize_email(email))
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        if usertype == 'A':
            user.is_college_admin = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):

        user = self.model(username=username, email = self.normalize_email(email))
        user.set_password(password)
        user.is_staff=True
        user.is_superuser=True
        
        user.save(using = self._db)
        return user
