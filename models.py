from django.db import models

class BaseItem(models.Model):
    '''Base Item model'''
    headline = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    content = models.TextField()
    keywords = models.CharField(max_length=255)
    year = models.DateField()
    url = models.SlugField(unique=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.headline

class Project(BaseItem):
    '''Project model'''
    author = models.CharField(max_length=255)
    stage = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    @models.permalink
    def get_absolute_url(self):
        return ('project', [str(self.url)])

class Reference(BaseItem):
    '''Reference model'''

    TYPE_CHOICES = (
        ('publication', 'Publication'),
        ('award', 'Award'),
        ('other', 'Other'),
    )

    project = models.ForeignKey(Project, related_name='references')
    type = models.CharField(max_length='20', choices=TYPE_CHOICES)

    @models.permalink
    def get_absolute_url(self):
        return ('reference', [str(self.url)])

class BaseImage(models.Model):
    '''Base Image model'''
    headline = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y', height_field='height', width_field='width')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.headline

class ProjectImage(BaseImage):
    '''Project image'''
    project = models.ForeignKey(Project, related_name='images')
    featured = models.BooleanField()

class ReferenceImage(BaseImage):
    '''Reference image'''
    reference = models.ForeignKey(Reference, related_name='images')
