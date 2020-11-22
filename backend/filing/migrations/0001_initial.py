# Generated by Django 3.1 on 2020-11-22 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cik",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cik_number", models.CharField(max_length=100)),
                ("filer_name", models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="Cusip",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cusip_number", models.CharField(max_length=100)),
                ("company_name", models.CharField(max_length=1000)),
                ("symbol", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Filing",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("form_type", models.CharField(max_length=100)),
                ("date_filed", models.DateField()),
                ("filename", models.CharField(max_length=300)),
                ("datafile", models.FileField(upload_to="")),
                (
                    "cik",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="filing_cik",
                        to="filing.cik",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FilingList",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("datafile", models.FileField(blank=True, null=True, upload_to="")),
                ("quarter", models.DateField()),
                ("filing_quarter", models.IntegerField()),
                ("filing_year", models.IntegerField()),
            ],
            options={"ordering": ("-quarter",),},
        ),
        migrations.CreateModel(
            name="Holding",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nameOfIssuer",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "titleOfClass",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "value",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=19,
                        null=True,
                        verbose_name="value",
                    ),
                ),
                (
                    "sshPrnamt",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=19,
                        null=True,
                        verbose_name="sshPrnamt",
                    ),
                ),
                (
                    "sshPrnamtType",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "investmentDiscretion",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("putCall", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "otherManager",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "sole",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=19,
                        null=True,
                        verbose_name="sole",
                    ),
                ),
                (
                    "shared",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=19,
                        null=True,
                        verbose_name="shared",
                    ),
                ),
                (
                    "nonee",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=19,
                        null=True,
                        verbose_name="nonee",
                    ),
                ),
                (
                    "cusip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cusip",
                        to="filing.cusip",
                    ),
                ),
                (
                    "filing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="filing",
                        to="filing.filing",
                    ),
                ),
            ],
            options={"ordering": ("filing__date_filed", "id"),},
        ),
        migrations.AddField(
            model_name="filing",
            name="filing_list",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="filinglist",
                to="filing.filinglist",
            ),
        ),
        migrations.CreateModel(
            name="CusipObservation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "cusip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cusip_for_observation",
                        to="filing.cusip",
                    ),
                ),
                (
                    "filing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="filing_observation",
                        to="filing.filing",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CikObservation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=1000)),
                (
                    "cik",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="observation_for_cik",
                        to="filing.cik",
                    ),
                ),
                (
                    "filing_list",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="filing_list_observation",
                        to="filing.filinglist",
                    ),
                ),
            ],
        ),
    ]
