from django.db.models import Case, When, F, FloatField, Value, Sum

from .models import Order


TONS_ANNOTATION = dict(
    blended_tons=Case(
        When(
            gross_weight__gt=0,
            then=(F("gross_weight") - F("tare_weight")) / Value(2000)
        ),
        default=F("total_tons"),
        output_field=FloatField()
    )
)

dry_tons = Order.objects.filter(
    blended_at__date__range=["2025-03-01", "2025-03-31"],
).annotate(
    **TONS_ANNOTATION
).values(
    "blend_status",
    "blended_at__date",
    "bag_type__kind",
).annotate(
    tons=Sum("blended_tons")
)