# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-12 17:18
from __future__ import unicode_literals

from django.db import migrations
from django.utils.text import slugify


def update_slugs(apps, schema_editor):
    Presentation = apps.get_model("schedule", "Presentation")
    ProposalBase = apps.get_model("proposals", "ProposalBase")
    Proposal = apps.get_model("proposals", "Proposal")
    for presentation in Presentation.objects.all():
        try:
            title = presentation.title or presentation.proposal_base.title
            presentation.slug = slugify(title)
            presentation.save()
        except Exception:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0018_presentation_slug'),
    ]

    operations = [
        migrations.RunPython(update_slugs),
    ]
