from django.contrib import admin
from .models import StudentProfile, ChatSession, Message, Feedback, InteractionEvent

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "area_interesse", "nivel_conhecimento", "created_at")
    search_fields = ("user__username", "user__email", "area_interesse")

class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    fields = ("role", "conteudo", "created_at")
    readonly_fields = ("created_at",)

@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "ativo", "created_at")
    inlines = [MessageInline]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sessao", "role", "conteudo", "created_at")

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("sessao", "mensagem_referencia", "gerado_pela_ia", "created_at")

@admin.register(InteractionEvent)
class InteractionEventAdmin(admin.ModelAdmin):
    list_display = ("tipo", "usuario", "sessao", "created_at")
    search_fields = ("tipo",)
    list_filter = ("tipo",)
