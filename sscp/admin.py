from django.contrib import admin
from sscp.models import TFilm, TDicomPrinter, TDicomWorkstation, TFilmSession, TJob
from sscp.models import TKiosk, TKioskFilmPaperInfo, TKioskParam, TOcrSetting
from sscp.models import TPatientFilmPrint, TPatientReport, TPatientReportPrint
from sscp.models import TPrintJob, TRisJob, TRisJobHistory
from sscp.models import TServer, TService, TSysFilmPaperType, TSysIni
from sscp.models import TSysPrintTimeConfig, TSysVersion, TVolume, TVpReport

admin.site.register(TFilm)
admin.site.register(TDicomPrinter)
admin.site.register(TDicomWorkstation)
admin.site.register(TFilmSession)
admin.site.register(TJob)
admin.site.register(TKiosk)
admin.site.register(TKioskFilmPaperInfo)
admin.site.register(TKioskParam)
admin.site.register(TOcrSetting)
admin.site.register(TPatientFilmPrint)
admin.site.register(TPatientReport)
admin.site.register(TPatientReportPrint)
admin.site.register(TPrintJob)
admin.site.register(TRisJob)
admin.site.register(TRisJobHistory)
admin.site.register(TServer)
admin.site.register(TService)
admin.site.register(TSysFilmPaperType)
admin.site.register(TSysIni)
admin.site.register(TSysPrintTimeConfig)
admin.site.register(TSysVersion)
admin.site.register(TVolume)
admin.site.register(TVpReport)