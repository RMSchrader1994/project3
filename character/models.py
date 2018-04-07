from django.db import models
from django.utils import timezone
from django.forms.models import ModelForm
from multiselectfield import MultiSelectField


class Character(models.Model):
    RACE_CHOICES = (
    ('breton','BRETON'),
    ('orc', 'ORC'),
    ('redguard','REDGUARD'),
    ('high elf','HIGH ELF'),
    ('wood elf','WOOD ELD'),
    ('khajiit', 'KHAJIIT'),
    ('argonian', 'ARGONIAN'),
    ('dark elf', 'DARK ELF'),
    ('nord', 'NORD')
    )
    
    CLASSES_CHOICES = (
    ('dragonknight', 'DRAGONKNIGHT'),
    ('sorcerer', 'SORCERER'),
    ('nightblade', 'NIGHTBLADE'),
    ('templar', 'TEMPLAR'),
    ('warden', 'WARDEN'),
    )
    
    GENDER_CHOICES = (
        ('m', 'MALE'),
        ('f', 'FEMALE'),
        )
        
    GUILD_CHOICES = (
        ('fighters', 'FIGHTERS'),
        ('mages', 'MAGES'),
        ('undaunted', 'UNDAUNTED'),
        ('thieves', 'THIEVES'),
        ('dark brotherhood', 'DARK BROTHERHOOD'),
        )
    

    """
    Here we'll define our Post model
    """

    # author is linked to a registered
    # user in the 'auth_user' table.
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    description = models.TextField()
    race = models.CharField(max_length=20, choices=RACE_CHOICES, default='breton')
    classes = models.CharField(max_length=20, choices=CLASSES_CHOICES, default='dragonknight')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='m')
    guild = MultiSelectField(choices=GUILD_CHOICES)
    published_date = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(max_length=30, blank=True, null=True)

  
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
    
    @property    
    def image(self):
        if self.race in ['orc', 'breton', 'redguard']: 
            return "images/race_Dc.png"
        if self.race in ['high elf', 'wood elf', 'khajiit']:
            return "images/race_Aldmeri_Dominion.png"
        if self.race in ['argonian', 'dark elf', 'nord']:
            return "images/race_Online_ebonheart_crest.png"