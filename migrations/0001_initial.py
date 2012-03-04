# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Project'
        db.create_table('portfolio_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('year', self.gf('django.db.models.fields.DateField')()),
            ('url', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('stage', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('portfolio', ['Project'])

        # Adding model 'Reference'
        db.create_table('portfolio_reference', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('year', self.gf('django.db.models.fields.DateField')()),
            ('url', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='references', to=orm['portfolio.Project'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length='20')),
        ))
        db.send_create_signal('portfolio', ['Reference'])

        # Adding model 'ProjectImage'
        db.create_table('portfolio_projectimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['portfolio.Project'])),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('portfolio', ['ProjectImage'])

        # Adding model 'ReferenceImage'
        db.create_table('portfolio_referenceimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('reference', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['portfolio.Reference'])),
        ))
        db.send_create_signal('portfolio', ['ReferenceImage'])


    def backwards(self, orm):
        
        # Deleting model 'Project'
        db.delete_table('portfolio_project')

        # Deleting model 'Reference'
        db.delete_table('portfolio_reference')

        # Deleting model 'ProjectImage'
        db.delete_table('portfolio_projectimage')

        # Deleting model 'ReferenceImage'
        db.delete_table('portfolio_referenceimage')


    models = {
        'portfolio.project': {
            'Meta': {'object_name': 'Project'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'stage': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'year': ('django.db.models.fields.DateField', [], {})
        },
        'portfolio.projectimage': {
            'Meta': {'object_name': 'ProjectImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['portfolio.Project']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'portfolio.reference': {
            'Meta': {'object_name': 'Reference'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'references'", 'to': "orm['portfolio.Project']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"}),
            'url': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'year': ('django.db.models.fields.DateField', [], {})
        },
        'portfolio.referenceimage': {
            'Meta': {'object_name': 'ReferenceImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'reference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['portfolio.Reference']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['portfolio']
