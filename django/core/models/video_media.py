from django.db import models


class VideoMedia(models.Model):
    class Status(models.TextChoices):
        UPLOADED_STARTED = 'UPLOADED_STARTED', 'Upload Iniciado'
        PROCESS_STARTED = 'PROCESSING_STARTED', 'Processamento Iniciado'
        PROCESS_FINISHED = 'PROCESSING_FINISHED', 'Processamento Finalizado'
        PROCESS_ERROR = 'PROCESSING_ERROR', 'Erro no Processamento'

    video_path = models.CharField(max_length=255, verbose_name='Vídeo')
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.UPLOADED_STARTED,
        verbose_name='Status')

    class Media:
        verbose_name = 'Mídia'
        verbose_name_plural = 'Mídias'
