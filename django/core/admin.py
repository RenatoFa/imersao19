from django.contrib import admin
from django.shortcuts import render
from django.urls import path, reverse
from django.utils.html import format_html

from core.models.tag import Tag
from core.models.video import Video
from core.models.video_media import VideoMedia

# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'is_published',
                    'num_likes', 'num_views', 'redirect_to_upload']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:id>/upload-video', self.upload_video,
                 name='core_video_upload')
        ]
        return custom_urls + urls

    def upload_video(self, request, id):
        return render(request, 'admin/core/upload_video.html')

    def redirect_to_upload(self, obj: Video):
        url = reverse('admin:core_video_upload', args=[obj.id])
        return format_html(f'<a href="{url}">Upload</a>')

    redirect_to_upload.short_description = 'Upload'


admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)
admin.site.register(VideoMedia)
