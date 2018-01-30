from django.db import models

ARC = (
    ('Forward', 'Forward'),
    ('Aft', 'Aft'),
    ('Port', 'Port'),
    ('Starboard', 'Starboard'),
)

COMPUTER_BONUS = (
    ('+0', '+0'),
    ('+1', '+1'),
    ('+1/+1', '+1/+1'),
    ('+1/+1/+1', '+1/+1/+1'),
    ('+1/+1/+1/+1', '+1/+1/+1/+1'),
    ('+2', '+2'),
    ('+2/+2', '+2/+2'),
    ('+2/+2/+2', '+2/+2/+2'),
    ('+2/+2/+2/+2', '+2/+2/+2/+2'),
    ('+3', '+3'),
    ('+3/+3', '+3/+3'),
    ('+3/+3/+3', '+3/+3/+3'),
    ('+3/+3/+3/+3', '+3/+3/+3/+3'),
    ('+4', '+4'),
    ('+4/+4', '+4/+4'),
    ('+4/+4/+4', '+4/+4/+4'),
    ('+5', '+5'),
    ('+5/+5', '+5/+5'),
    ('+5/+5/+5', '+5/+5/+5'),
    ('+6', '+6'),
    ('+6/+6', '+6/+6'),
    ('+7', '+7'),
    ('+7/+7', '+7/+7'),
    ('+8', '+8'),
    ('+8/+8', '+8/+8'),
)

WEIGHT = (
    ('Light', 'Light'),
    ('Heavy', 'Heavy'),
    ('Capital', 'Capital'),
)

TYPE = (
    ('Direct Fire', 'Direct Fire'),
    ('Tracking', 'Tracking'),
)

RANGES = (
    ('Short', 'Short'),
    ('Medium', 'Medium'),
    ('Long', 'Long'),
)

DICE = (
    ('d4', 'd4'),
    ('d6', 'd6'),
    ('d8', 'd8'),
    ('d10', 'd10'),
    ('d12', 'd12'),
    ('d20', 'd20'),
)


class Size(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Size'
    )
    length = models.PositiveIntegerField
    weight = models.PositiveIntegerField
    ac_tl_mod = models.IntegerField


class Tier(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Tier',
    )
    build_points = models.PositiveIntegerField(default=0)
    special = models.BooleanField


class Maneuverability(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Tier',
    )
    distance = models.PositiveIntegerField(default=2)
    pilot_modifier = models.IntegerField(default=0)


class Frame(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Frame',
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
    )
    maneuverability = models.ForeignKey(
        Maneuverability,
        on_delete=models.CASCADE,
    )
    hitpoints = models.PositiveIntegerField(default=0)
    DT = models.PositiveIntegerField(default=0)
    CT = models.PositiveIntegerField(default=0)
    arc = models.CharField(
        max_length=100,
        choices=ARC,
    )
    expansions = models.PositiveIntegerField(default=0)
    min_crew = models.PositiveIntegerField(default=0)
    max_crew = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0)


class Core(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Power Core',
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
    )
    pcu = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0)


class Thruster(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Thruster',
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
    )
    speed = models.PositiveIntegerField(default=0)
    pilot_mod = models.IntegerField(default=0)
    pcu = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0)


class Armor(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Armor',
    )
    ac_bonus = models.PositiveIntegerField(default=0)
    # special = models.ForeignKey
    cost = models.PositiveIntegerField(default=0)


class Computer(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Computer',
    )
    bonus = models.CharField(
        max_length=100,
        choices=COMPUTER_BONUS,
    )
    nodes = models.PositiveIntegerField(default=0)
    pcu = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0)


class CrewQuarter(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Quarters',
    )
    cost = models.PositiveIntegerField(default=0)


class Countermeasure(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Countermeasure',
    )
    bonus = models.PositiveIntegerField(default=0)
    pcu = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0)


class DriftEngine(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Drift Engine',
    )
    rating = models.PositiveIntegerField(default=0)
    min_pcu = models.PositiveIntegerField(default=0)
    max_size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
    )


class ExpansionBay(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Expansion Bay',
    )
    pcu = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0)


class Security(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Security',
    )
    cost = models.PositiveIntegerField(default=0)


class Sensors(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Sensor',
    )
    range = models.CharField(
        max_length=100,
        choices=RANGES,
    )
    modifier = models.IntegerField(default=0)
    cost = models.PositiveIntegerField(default=0)


class Shields(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Shield',
    )
    shield_points = models.PositiveIntegerField(default=0)
    regen = models.PositiveIntegerField(default=0)
    pcu = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0)


class Weapons(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Name',
    )
    weight = models.CharField(
        max_length=100,
        choices=WEIGHT,
    )
    type = models.CharField(
        max_length=100,
        choices=TYPE,
    )
    range = models.CharField(
        max_length=100,
        choices=RANGES,
    )
    speed = models.PositiveIntegerField(default=0)
    damage_number = models.PositiveIntegerField(default=0)
    damage_die = models.CharField(
        max_length=100,
        verbose_name='Damage Die',
        choices=DICE,
    )
    pcu = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0)
    # properties = models.ForeignKey(
    #     Properties,
    #     on_delete=models.CASCADE,
    # )


class Starship(models.Model):
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    core = models.ForeignKey(Core, on_delete=models.CASCADE)
    thrusters = models.ForeignKey(Thruster, on_delete=models.CASCADE)
    armor = models.ForeignKey(Armor, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    crew_quarters = models.ForeignKey(CrewQuarter, on_delete=models.CASCADE)
    countermeasures = models.ForeignKey(Countermeasure, on_delete=models.CASCADE)
    drift_engine = models.ForeignKey(DriftEngine, on_delete=models.CASCADE)
    expansion_bays = models.ForeignKey(ExpansionBay, on_delete=models.CASCADE)
    security = models.ForeignKey(Security, on_delete=models.CASCADE)
    sensors = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    shields = models.ForeignKey(Shields, on_delete=models.CASCADE)
    weapons = models.ForeignKey(Weapons, on_delete=models.CASCADE)

