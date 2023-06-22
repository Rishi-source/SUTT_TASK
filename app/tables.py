import django_tables2 as tables
from .models import User

class UserTable(tables.Table):
    username = tables.Column()
    email = tables.Column()

    class Meta:
        model = User
        fields = ('username', 'name')
