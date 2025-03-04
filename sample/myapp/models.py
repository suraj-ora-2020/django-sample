#
#This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

#from django.conf import settings
#import logging
#import sqlalchemy.pool as pool
#pool_initialized=False
#import django.contrib.auth
#from django.contrib.auth import load_backend

#from django.db.backends.base.base import BaseDatabaseWrapper

#conn = BaseDatabaseWrapper.connection

#print(BaseDatabaseWrapper.connection)

#print(type(load_backend))
#def init_pool():
#     if not globals().get('pool_initialized', False):
#         global pool_initialized
#         pool_initialized = True
#         try:
#             backendname = settings.DATABASES['default']['ENGINE']
#            print(backendname)
#             backend = load_backend(backendname)

             #replace the database object with a proxy.
#             backend.Database = pool.manage(backend.Database)


#             backend.DatabaseError = backend.Database.DatabaseError
#             backend.IntegrityError = backend.Database.IntegrityError
#             logging.info("Connection Pool initialized")
#         except:
#             logging.exception("Connection Pool initialization error")

#Now call init_pool function to initialize the connection pool. No change required in the
# Django code.
#init_pool()



class Bonus(models.Model):
    ename = models.CharField(max_length=10, blank=True, null=True)
    job = models.CharField(max_length=9, blank=True, null=True)
    sal = models.FloatField(blank=True, null=True)
    comm = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bonus'


class Dept(models.Model):
    deptno = models.IntegerField()
    dname = models.CharField(max_length=14, blank=True, null=True)
    loc = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dept'


class emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=10, blank=True, null=True)
    job = models.CharField(max_length=9, blank=True, null=True)
    sal = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp'


class Salgrade(models.Model):
    grade = models.FloatField(blank=True, null=True)
    losal = models.FloatField(blank=True, null=True)
    hisal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salgrade'
