from django.db import models

class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	birth_date = models.DateField()
	death_date = models.DateField()
	biography = models.TextField(max_length=3000)
	
	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name)
	
class Piece(models.Model):
	DIFFICULTY_CHOICES = (
		('1', 'easy'),
		('2', 'easy/intermediate'),
		('3', 'intermediate'),
		('4', 'intermediate/hard'),
		('5', 'hard')
	)
	title = models.CharField(max_length=200)
	publication_date = models.DateField()
	key = models.CharField(max_length=50)
	publisher = models.CharField(max_length=100)
	meters = models.CharField(max_length=50)
	ranges = models.TextField(max_length=1000)
	note_values = models.CharField(max_length=100)
	description = models.TextField(max_length=3000)
	nyssma_level = models.IntegerField(verbose_name="NYSSMA Level")
	florida_state_level = models.IntegerField(verbose_name="Florida State Level")
	texas_state_level = models.IntegerField(verbose_name="Texas State Level")
	composer = models.ForeignKey(Person, related_name="%(class)s_composer")
	arranger = models.ForeignKey(Person, related_name="%(class)s_person_arranger")
	difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
	
	class Meta:
		abstract = True
	
	def __unicode__(self):
		return self.title

class BandPiece(Piece):
	YEAR_CHOICES = (
		('4', '4th'),
		('5', '5th'),
		('6', '6th'),
		('7', '7th'),
		('8', '8th'),
		('9', '9th'),
		('10', '10th'),
		('11', '11th'),
		('12', '12th'),
		('13', 'Honors/College')
	)
	grade = models.CharField(max_length=10, choices=YEAR_CHOICES)

class OrchestraPiece(Piece):
	YEAR_CHOICES = (
		('4', '4th'),
		('5', '5th'),
		('6', '6th'),
		('7', '7th'),
		('8', '8th'),
		('9', '9th'),
		('10', '10th'),
		('11', '11th'),
		('12', '12th'),
		('13', 'Honors/College')
	)
	grade = models.CharField(max_length=10, choices=YEAR_CHOICES)

class ChoirPiece(Piece):
	CHOIR_CATEGORY_CHOICES = (
		('satb', 'SATB'),
	)
	category = models.CharField(max_length=20, choices=CHOIR_CATEGORY_CHOICES)

class SoloPiece(Piece):
	INSTRUMENT_CHOICES = (
		('percussion', 'THE ONLY ONE (percussion)'),
	)
	instrument = models.CharField(max_length=20, choices=INSTRUMENT_CHOICES)

class SmallEnsemblePiece(Piece):
	SMALL_ENSEMBLE_CATEGORY_CHOICES = (
		('2', 'Duet'),
		('3', 'Trio'),
		('4', 'Quartet'),
		('5', 'Quintet'),
		('6', 'Sextet'),
		('7', 'Other Ensemble')
	)
	small_ensemble_category = models.CharField(max_length=1, choices=SMALL_ENSEMBLE_CATEGORY_CHOICES)
