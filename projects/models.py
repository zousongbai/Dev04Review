from django.db import models


# Create your models here.
# 1����������Ӧ��projects/models.py�ļ��У�����������ģ��
# 2��һ������ģ�����Ӧһ�����ݱ�
# 3������ģ���࣬��Ҫ�̳�Model�������Model���࣬���̳оͲ�������ģ���࣬������ͨ����
# 4��������ģ�����У���ӵ������ԣ�Field��������Ӧ���ݱ��е��ֶ�
# 5�����������ݿ�ģ����֮����ҪǨ�Ʋ����������ݱ�
# ������Ǩ�ƽű�������projects/migrationsĿ¼�У�python manage.py makemigrations
# ��ִ��Ǩ�ƽű���python manage.py migrate
# ����������ѡ���ô�Ὣ������Ӧ�ý���Ǩ��
# 6�����Զ������ֶ���Ϊid�������ԣ��������������ǿ�
# ��1������һ������ģ���࣬��Ҫ�̳�Model�������Model���࣬���̳оͲ�������ģ���࣬������ͨ����
class Projects(models.Model):
    # ��2���������
    # ��ģ��������Ϊ��Ӧ��������ĸ��д����Projects
    # ����Ҫ�̳�models���е�Model

    # ��3�����������������Ե���ʽ������ݱ���ֶ�
    # ����Ŀ����
    name = models.CharField(max_length=200)
    # ��ע��
    # 1��CharField����Ӧ���ݿ���ַ���varchar
    # 2���������ַ�������󳤶�

    # ����Ŀ�������Ϣ
    leader = models.CharField(max_length=50)

    # ��4�������ģ����������ݿ�ģ����֮����ҪǨ�Ʋ����������ݱ�
    # ������Ǩ�ƽű�������projects/migrationsĿ¼�У�python manage.py makemigrations
    # ��ִ��Ǩ�ƽű���python manage.py migrate
