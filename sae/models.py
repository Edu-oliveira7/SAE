import uuid
from django.db import models
from django.contrib.auth.models import User

class TimeStampedUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class StudentProfile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    nome_exibicao = models.CharField(max_length=120, blank=True)
    area_interesse = models.CharField(max_length=120, blank=True)
    objetivos = models.CharField(max_length=240, blank=True)
    nivel_conhecimento = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return self.nome_exibicao or self.user.get_username()


class ChatSession(TimeStampedUUIDModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_sessoes")
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return f"Sessão {self.id} - {self.usuario}"


class Message(TimeStampedUUIDModel):
    sessao = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name="mensagens")
    role = models.CharField(max_length=20, choices=[("user", "Usuário"), ("assistant", "IA")])
    conteudo = models.TextField()
    def __str__(self):
        return f"{self.role} - {self.sessao_id}"


class Feedback(TimeStampedUUIDModel):
    sessao = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name="feedbacks")
    mensagem_referencia = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True, blank=True)
    reflexao = models.TextField(blank=True)
    gerado_pela_ia = models.BooleanField(default=False)
    def __str__(self):
        return f"Feedback {self.id} - Sessão {self.sessao_id}"


class InteractionEvent(TimeStampedUUIDModel):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    sessao = models.ForeignKey(ChatSession, on_delete=models.SET_NULL, null=True, blank=True)
    mensagem = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.CharField(max_length=40)
    payload = models.JSONField(blank=True, null=True)
    def __str__(self):
        return f"{self.tipo} @ {self.created_at:%Y-%m-%d %H:%M}"
