from musicLit.musicLitDB.models import Person
from musicLit.musicLitDB.models import BandPiece
from musicLit.musicLitDB.models import OrchestraPiece
from musicLit.musicLitDB.models import ChoirPiece
from musicLit.musicLitDB.models import SoloPiece
from musicLit.musicLitDB.models import SmallEnsemblePiece
from django.contrib import admin

admin.site.register(Person)
admin.site.register(BandPiece)
admin.site.register(OrchestraPiece)
admin.site.register(ChoirPiece)
admin.site.register(SoloPiece)
admin.site.register(SmallEnsemblePiece)
