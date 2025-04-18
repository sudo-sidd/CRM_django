# Generated by Django 5.1.6 on 2025-03-09 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finished_goods', '0004_boxpaperrequirements_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_name', models.CharField(max_length=100, unique=True)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('breadth', models.DecimalField(decimal_places=2, max_digits=10)),
                ('height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('flute_type', models.CharField(choices=[('A', 'A Flute'), ('B', 'B Flute'), ('C', 'C Flute')], max_length=1)),
                ('num_plies', models.IntegerField(choices=[(3, '3 Ply'), (5, '5 Ply'), (7, '7 Ply')])),
                ('print_color', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoxOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=50, unique=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('pending', 'Pending Approval'), ('approved', 'Approved'), ('in_production', 'In Production'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='draft', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('delivery_date', models.DateField()),
                ('notes', models.TextField(blank=True)),
                ('box_template', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finished_goods.boxtemplate')),
            ],
        ),
        migrations.CreateModel(
            name='ManufacturingCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('machine_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('labor_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('overhead_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('profit_margin', models.DecimalField(decimal_places=2, max_digits=5)),
                ('suggested_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('box_order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='finished_goods.boxorder')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_paper_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bottom_paper_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('flute_paper_weight', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('middle_paper_weight', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('paper_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gum_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ink_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('calculated_at', models.DateTimeField(auto_now=True)),
                ('box_order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='finished_goods.boxorder')),
            ],
        ),
    ]
