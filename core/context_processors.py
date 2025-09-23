from .models import HomepageHero


def homepage_hero(request):
    """
    Adds the active homepage hero (and its phrases) to all templates.
    """
    hero = (
        HomepageHero.objects.filter(is_active=True).prefetch_related("phrases").first()
    )
    return {"homepage_hero": hero}
