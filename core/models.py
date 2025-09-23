from django.db import models


class HomepageHero(models.Model):
    """Model for the homepage hero section."""

    title = models.CharField(
        max_length=200, help_text="Main title (e.g. 'Hi, I’m John Doe')."
    )
    subtitle = models.CharField(
        max_length=500, help_text="Subtitle or role (e.g. 'Full-Stack Developer')."
    )
    background_image = models.ImageField(
        upload_to="hero_backgrounds/",
        help_text="Background image for the hero section.",
    )
    profile_image = models.ImageField(
        upload_to="profile_image/",
        help_text="Background image for the hero section.",
    )
    is_active = models.BooleanField(
        default=True, help_text="Toggle this hero section on/off."
    )

    def save(self, *args, **kwargs):
        # If this hero is marked active, deactivate all others
        if self.is_active:
            HomepageHero.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class HeroPhrase(models.Model):
    """Phrases that rotate in the homepage hero section."""

    hero = models.ForeignKey(
        HomepageHero, related_name="phrases", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=150)
    order = models.PositiveIntegerField(
        default=0, help_text="Display order of the phrase."
    )

    class Meta:
        ordering = ["order"]

    def save(self, *args, **kwargs):
        # If this is a new phrase and order not set, auto-increment
        if self._state.adding and self.order == 0:
            last_order = (
                HeroPhrase.objects.filter(hero=self.hero)
                .order_by("-order")
                .values_list("order", flat=True)
                .first()
            )
            self.order = (last_order or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text
