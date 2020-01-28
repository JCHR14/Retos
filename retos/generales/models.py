from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class OwnedModel(models.Model):
    owner = models.ForeignKey(User,
    on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True

class Team(OwnedModel):
    team_id = models.AutoField(_("id"), primary_key=True)
    name = models.CharField(_("name"), max_length=100)
    longitude = models.DecimalField(_("longitude"), max_digits=9, decimal_places=6)
    latitude  = models.DecimalField(_("latitude"), max_digits=9, decimal_places=6)
    status = models.NullBooleanField(_("status"), default=True)
    logo = models.FileField(_("logo"), upload_to='images/teams/',max_length=500)
    date_created = models.DateTimeField(_("date_created"), auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(_("date_updated"), auto_now=True, auto_now_add=False)
    #user_created = models.ForeignKey(User, verbose_name=_("user_created"), on_delete=models.CASCADE)
    user_updated = models.ForeignKey(User, verbose_name=_("user_updated"), on_delete=models.CASCADE, related_name ='updated_team')
    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")
        db_table = 'teams'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Team_detail", kwargs={"pk": self.pk})

class CategoryTeam(OwnedModel):
    CATEGORIES = [
        (0, 'Categoría Unica'),
        (1, 'Primera categoría Varones'),
        (2, 'Primera categoría Mujeres'),
        (3, 'Segunda categoria Varones'),
        (4, 'Segunda categoria Mujeres'),
        (5, 'Juvenil Varones'),
        (6, 'Juvenil Mujeres'),
        (7, 'Mosco Varones'),
        (8, 'Mosco Mujeres'),
        (9, 'Pre-mosco Varones'),
        (10, 'Pre-mosco Mujeres'),
    ]
    category_id = models.AutoField(_("id"), primary_key=True)
    category = models.IntegerField(_("category"), choices=CATEGORIES)
    team = models.ForeignKey(Team, verbose_name=_("team"), on_delete=models.CASCADE)
    uniform_color = models.CharField(_("uniform_color"), max_length=50, default='')
    class Meta:
        verbose_name = _("CategoryTeam")
        verbose_name_plural = _("CategoryTeams")
        db_table = 'category_team'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("categoryTeam_detail", kwargs={"pk": self.pk})

class KindOfTeam(OwnedModel):
    TYPES = [
        (1, 'Futbol 11'),
        (2, 'Futbol sala'),
        (3, 'Futbol 8'),
        (4, 'Futbol 5'),
    ]
    kindof_id = models.AutoField(_("id"), primary_key=True)
    kindof = models.IntegerField(_("kindof"), choices=TYPES)
    team = models.ForeignKey(Team, verbose_name=_("team"), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("KindOfTeam")
        verbose_name_plural = _("KindOfTeams")
        db_table = 'kindof_team'

    def __str__(self):
        return self.kindof

    def get_absolute_url(self):
        return reverse("KindOfTeam_detail", kwargs={"pk": self.pk})

class UsersTeam(OwnedModel):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE, related_name = 'team_staff_player')
    team = models.ForeignKey(Team, verbose_name=_("team"), on_delete=models.CASCADE)
    date_inserted = models.DateTimeField(_("date_inserted"), auto_now=False, auto_now_add=True)
    status = models.NullBooleanField(_("status"), default=True)

    class Meta:
        unique_together = ('user', 'team',)
        verbose_name = _("UsersTeam")
        verbose_name_plural = _("UsersTeams")
        db_table = 'users_team'

    def __str__(self):
        return '{} - {}'.format(self.user, self.team.name)

    def get_absolute_url(self):
        return reverse("UsersTeam_detail", kwargs={"pk": self.pk})

class Challenge(OwnedModel):
    STATUS = [
        (1, 'Solicitado'),
        (2, 'Aceptado'),
        (3, 'Reprogramado'),
        (4, 'No Aceptado'),
        (4, 'Cancelado'),
    ]
    challenge_id = models.AutoField(_("id"), primary_key=True)
    local = models.ForeignKey(Team, verbose_name=_("local"), on_delete=models.CASCADE)
    visitor = models.ForeignKey(Team, verbose_name=_("visitor"), on_delete=models.CASCADE, related_name='visitor_team')
    status = models.IntegerField(_("status"), choices=STATUS)
    date = models.DateTimeField(_("date"), auto_now=False, auto_now_add=False)
    bond = models.PositiveIntegerField(_("bond"))
    date_created = models.DateTimeField(_("date_created"), auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(_("date_updated"), auto_now=True, auto_now_add=False)
    #user_created = models.ForeignKey(User, verbose_name=_("user_created"), on_delete=models.CASCADE)
    user_updated = models.ForeignKey(User, verbose_name=_("user_updated"), on_delete=models.CASCADE, related_name ='updated_challange')

    class Meta:
        verbose_name = _("Challenge")
        verbose_name_plural = _("Challenges")
        db_table = 'challenge'

    def __str__(self):
        return 'L:{} vs V:{}'.format(self.local, self.visitor)

    def get_absolute_url(self):
        return reverse("Challenge_detail", kwargs={"pk": self.pk})

class ChallengeComment(OwnedModel):
    comment_id = models.AutoField(_("id"), primary_key=True)
    comment = models.CharField(_("comment"), max_length=50)
    date = models.DateTimeField(_("date"), auto_now=False, auto_now_add=True)
    deleted = models.NullBooleanField(_("deleted"), default = False)
    #user_created = models.ForeignKey(User, verbose_name=_("user_created"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("ChallengeComment")
        verbose_name_plural = _("ChallengeComments")
        db_table = 'challenge_comment'

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("ChallengeComment_detail", kwargs={"pk": self.pk})

class Game(OwnedModel):
    game_id = models.AutoField(_("id"), primary_key=True)
    challenge = models.ForeignKey(Challenge, verbose_name=_("challenge"), on_delete=models.CASCADE)
    local_category = models.ForeignKey(CategoryTeam, verbose_name=_("local_category"), on_delete=models.CASCADE)
    visitor_category = models.ForeignKey(CategoryTeam, verbose_name=_("visitor_category"), on_delete=models.CASCADE, related_name='visitor_team_category')
    date = models.DateTimeField(_("date"), auto_now=False, auto_now_add=False)
    status = models.CharField(_("status"), max_length=50)
    class Meta:
        verbose_name = _("Game")
        verbose_name_plural = _("Games")
        db_table = 'game'

    def __str__(self):
        return 'L:{} vs V:{}'.format(self.local_category, self.visitor_category)

    def get_absolute_url(self):
        return reverse("Game_detail", kwargs={"pk": self.pk})