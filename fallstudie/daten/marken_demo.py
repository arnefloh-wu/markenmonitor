# -*- coding: utf-8 -*-
"""Fiktive Marken und Kategoriebegriffe fuer den Demonstrationsdatensatz.

ALLE Namen sind frei erfunden. Sie sind so gewaehlt, dass sie wie
Suesswarenmarken klingen, aber keiner realen Marke entsprechen. Ziel ist eine
Fallstudie, die Methode und Darstellung zeigt, ohne Kundendaten zu beruehren.

Die Codes entsprechen dem Raster der echten Studie, damit die Pipeline
unveraendert laeuft: 1-20 plus 90-92 landesspezifisch, 99 die Ausweichoption.
"""

# Code -> (Name, in AT im Raster, in DE im Raster)
MARKEN = {
    '1':  ('Balmo',       1, 1),
    '2':  ('Nutrika',     1, 1),
    '3':  ('Cocoway',     1, 1),
    '4':  ('Granova',     1, 1),
    '5':  ('Alpzart',     1, 0),   # nur AT, wie eine lokale Traditionsmarke
    '6':  ('Hazelo',      1, 1),
    '7':  ('Ketolino',    1, 0),   # nur AT
    '8':  ('Vollmond',    1, 1),
    '9':  ('Knusperli',   1, 1),
    '10': ('Almgold',     1, 1),   # AT-Traditionsmarke, in DE schwach
    '11': ('Orbix',       1, 1),
    '12': ('Lunara',      1, 1),
    '13': ('ZINTO',       1, 1),   # die Marke der Fallstudie
    '14': ('Nordfit',     1, 1),
    '15': ('Cacaolu',     1, 1),
    '16': ('Snapup',      1, 1),
    '17': ('Crunchor',    1, 1),
    '18': ('Protera',     1, 1),
    '19': ('Nutriq',      1, 1),
    '20': ('Sportlab',    1, 0),   # nur AT
    '90': ('Barvita',     0, 1),   # nur DE
    '91': ('Sweetless',   0, 1),   # nur DE
    '92': ('Zweibiss',    0, 1),   # nur DE
}
HELD = '13'
HELD_NAME = 'ZINTO'

# Marken, die im Raster 2022 standen (18 Stueck, wie in der echten Welle)
MARKEN_2022 = ['1','2','3','4','5','20','6','7','8','9','10','11','12','13',
               '14','15','16','17']

# Marken, die nur im freien Text auftauchen - das Gegenstueck zu den Marken,
# die nachtraeglich ins Raster aufgenommen wurden.
AUSSERHALB = ['Riegelo', 'Choco Star', 'Nusslé', 'Felsbrocken', 'Kakaono',
              'Bergnuss', 'Schoko Max']

# Eigenmarken und Haendlernennungen, die in offenen Antworten vorkommen
RAUSCHEN = ['Eigenmarken', 'Supermarkt-Eigenmarke', 'weiss nicht', 'keine',
            'Bio-Laden', 'Drogerie']
