"""Physik-LK-App mit Wissen, das per Byteindex aus wissen.txt geladen wird."""

from gint import *
# Automatisch aus physchem-final.py erzeugter Byteindex.

MODES = [
    ('Theorie', 0, 19),
    ('Formeln nach Groessen', 19, 77),
    ('Formeln nach Themen', 96, 10),
]

SECTIONS = [
    ('Ueberblick', 0, 1),
    ('Mechanik', 1, 1),
    ('Elektrisches Feld', 2, 1),
    ('Magnetfeld / Teilchen', 3, 4),
    ('Induktion', 7, 3),
    ('Lenz / Wirbelstroeme', 10, 2),
    ('Spule / Trafo', 12, 3),
    ('Wechselstrom / RLC', 15, 8),
    ('Konzepte / Relativitaet', 23, 1),
    ('Praktikum / Einheiten', 24, 2),
    ('Lehrer-Material', 26, 1),
    ('Lexikon: Konstanten / Material', 27, 10),
    ('Lexikon: Induktion / Spule', 37, 8),
    ('Lexikon: Wechselstrom / RLC', 45, 10),
    ('Lexikon: Mechanik', 55, 8),
    ('Lexikon: Felder Basis', 63, 5),
    ('Lexikon: Teilchen erweitert', 68, 8),
    ('Lexikon: Lehrer-Material', 76, 8),
    ('Lexikon: WSK-Folien', 84, 8),
    ('A', 92, 5),
    ('B', 97, 6),
    ('B_max', 103, 2),
    ('C', 105, 2),
    ('DeltaA', 107, 2),
    ('DeltaB', 109, 2),
    ('DeltaI', 111, 2),
    ('DeltaPhi', 113, 2),
    ('DeltaPhi_phase', 115, 3),
    ('E', 118, 2),
    ('E0', 120, 2),
    ('E_cap', 122, 3),
    ('E_kin', 125, 4),
    ('E_mag', 129, 3),
    ('E_pot', 132, 2),
    ('F', 134, 3),
    ('F_G', 137, 2),
    ('F_L', 139, 2),
    ('F_R', 141, 2),
    ('F_el', 143, 2),
    ('F_r', 145, 2),
    ('H', 147, 3),
    ('I', 150, 10),
    ('I0', 160, 3),
    ('I1', 163, 2),
    ('I2', 165, 3),
    ('I_eff', 168, 3),
    ('L', 171, 4),
    ('N', 175, 4),
    ('N1', 179, 2),
    ('N2', 181, 2),
    ('P', 183, 3),
    ('P_V', 186, 3),
    ('Phi', 189, 3),
    ('Phi_E', 192, 2),
    ('Q', 194, 3),
    ('Q_blind', 197, 2),
    ('R', 199, 5),
    ('S', 204, 2),
    ('T', 206, 2),
    ('U', 208, 2),
    ('U0', 210, 2),
    ('U1', 212, 2),
    ('U2', 214, 2),
    ('U_eff', 216, 2),
    ('U_ind', 218, 10),
    ('U_max', 228, 2),
    ('W', 230, 2),
    ('W_el', 232, 2),
    ('X_C', 234, 2),
    ('X_L', 236, 2),
    ('Z', 238, 3),
    ('a', 241, 3),
    ('a_r', 244, 2),
    ('beta', 246, 2),
    ('cos_phi', 248, 2),
    ('d', 250, 3),
    ('eps0', 253, 1),
    ('eps_r', 254, 2),
    ('eta', 256, 3),
    ('f', 259, 3),
    ('f0', 262, 2),
    ('gamma', 264, 2),
    ('h', 266, 3),
    ('l', 269, 8),
    ('l_Draht', 277, 2),
    ('m', 279, 2),
    ('mu0', 281, 1),
    ('mu_r', 282, 3),
    ('omega', 285, 5),
    ('p', 290, 2),
    ('q_m', 292, 2),
    ('r', 294, 3),
    ('rho', 297, 2),
    ('tau', 299, 2),
    ('v', 301, 4),
    ('v_filter', 305, 2),
    ('Induktion / Fluss', 307, 31),
    ('Spule / Selbstinduktion', 338, 46),
    ('Kondensator', 384, 22),
    ('Wechselstrom / RLC', 406, 44),
    ('Transformator', 450, 16),
    ('Elektrisches Feld', 466, 11),
    ('Magnetfeld / Teilchen', 477, 19),
    ('Mechanik', 496, 21),
    ('Relativitaet', 517, 3),
    ('Sonstige', 520, 2),
]

ENTRIES = [
    ('Sachsen LK 11 Ueberblick', 0),
    ('Mechanik komplett', 1),
    ('Elektrisches Feld / Kondensator', 2),
    ('Magnetfeld / geladene Teilchen', 3),
    ('Teilchenbeschleuniger', 4),
    ('Elektron im B-Feld', 5),
    ('Massenspektrometer / Filter', 6),
    ('Induktion / magnetischer Fluss', 7),
    ('IQB Parameter A-F', 8),
    ('Induktion mit Ableitungen', 9),
    ('Lenzsche Regel / Wirbelstroeme', 10),
    ('Wirbelstroeme Anwendungen', 11),
    ('Selbstinduktion / Spule', 12),
    ('Transformator', 13),
    ('Transformator erweitert', 14),
    ('Ohmsches Bauelement im WSK', 15),
    ('Kondensator im WSK', 16),
    ('Spule im WSK', 17),
    ('Wirk- und Blindwiderstand', 18),
    ('Zeigerdiagramm', 19),
    ('RLC-Reihenschaltung / Siebkreis', 20),
    ('Resonanz / Thomson', 21),
    ('Energieumwandlung im RLC', 22),
    ('Elektromagnetismus-Konzepte', 23),
    ('Praktikum / Messunsicherheiten', 24),
    ('Einheitenwissen / typische Fehler', 25),
    ('Lehrer-Material Ueberblick', 26),
    ('mu0 - magnetische Feldkonstante', 27),
    ('mu_r - relative Permeabilitaet', 28),
    ('H - magnetische Feldstaerke', 29),
    ('B - magnetische Flussdichte', 30),
    ('Phi - magnetischer Fluss', 31),
    ('eps0 - elektrische Feldkonstante', 32),
    ('eps_r - relative Permittivitaet', 33),
    ('rho - spezifischer elektrischer Widerstand', 34),
    ('e - Elementarladung', 35),
    ('c - Lichtgeschwindigkeit', 36),
    ('U_ind - Induktionsspannung', 37),
    ('N - Windungszahl', 38),
    ('A - wirksame Flaeche', 39),
    ('alpha - Winkel', 40),
    ('Delta Phi - Flussaenderung', 41),
    ('dPhi/dt - momentane Flussaenderungsrate', 42),
    ('L - Induktivitaet', 43),
    ('E_mag - magnetische Energie', 44),
    ('R - ohmscher Wirkwiderstand', 45),
    ('X_L - induktiver Blindwiderstand', 46),
    ('X_C - kapazitiver Blindwiderstand', 47),
    ('Z - Impedanz / Scheinwiderstand', 48),
    ('Delta phi - Phasenverschiebung', 49),
    ('omega - Kreisfrequenz', 50),
    ('f0 - Resonanzfrequenz', 51),
    ('T - Periodendauer / Schwingungsdauer', 52),
    ('U_eff - Effektivspannung', 53),
    ('I_eff - Effektivstrom', 54),
    ('E_kin - Bewegungsenergie', 55),
    ('E_pot - Lageenergie', 56),
    ('E_sp - Spannenergie', 57),
    ('W - Arbeit', 58),
    ('P - Leistung', 59),
    ('p - Impuls', 60),
    ('F - Kraft', 61),
    ('a - Beschleunigung', 62),
    ('E - elektrische Feldstaerke', 63),
    ('q - elektrische Ladung', 64),
    ('C - Kapazitaet', 65),
    ('F_L - Lorentzkraft', 66),
    ('r - Kreisbahnradius', 67),
    ('q - Ladung', 68),
    ('m - Masse', 69),
    ('q/m - spezifische Ladung', 70),
    ('r - Kreisbahnradius', 71),
    ('v - Teilchengeschwindigkeit', 72),
    ('E_kin - kinetische Energie', 73),
    ('gamma - Lorentzfaktor', 74),
    ('U_B - Beschleunigungsspannung', 75),
    ('q/m - spezifische Ladung', 76),
    ('v_filter - Filtergeschwindigkeit', 77),
    ('rho - spezifischer Widerstand', 78),
    ('H - magnetische Feldstaerke', 79),
    ('mu_r - relative Permeabilitaet', 80),
    ('P_V - Verlustleistung', 81),
    ('gamma - Lorentzfaktor', 82),
    ('E_kin - kinetische Energie geladener Teilchen', 83),
    ('R - ohmscher Wirkwiderstand', 84),
    ('X_L - induktiver Blindwiderstand', 85),
    ('X_C - kapazitiver Blindwiderstand', 86),
    ('Z - Impedanz / Scheinwiderstand', 87),
    ('Delta phi - Phasenverschiebung', 88),
    ('f0 - Resonanzfrequenz', 89),
    ('T - Schwingungsdauer', 90),
    ('omega - Kreisfrequenz', 91),
    ('A - Flaeche aus Induktivitaet', 92),
    ('A - Kreisflaeche aus Radius', 93),
    ('A - Kreisflaeche aus Durchmesser', 94),
    ('A - Rechteckflaeche', 95),
    ('A - Drahtquerschnitt aus Widerstand', 96),
    ('B - B aus Feldstaerke und Permeabilitaet', 97),
    ('B - magnetische Flussdichte aus Fluss', 98),
    ('B - Magnetfeld einer langen Spule', 99),
    ('B - B aus Lorentzkraft auf Ladung', 100),
    ('B - B aus Kraft auf stromdurchflossenen Leiter', 101),
    ('B - B aus Bewegungsinduktion', 102),
    ('B_max - B-Amplitude aus Generator', 103),
    ('B_max - B-Amplitude aus Dreiecksignal', 104),
    ('C - Kapazitaet aus X_C', 105),
    ('C - Kapazitaet Plattenkondensator', 106),
    ('DeltaA - Flaechenaenderung aus Induktion', 107),
    ('DeltaA - Flaechenaenderung', 108),
    ('DeltaB - B-Aenderung aus Induktion', 109),
    ('DeltaB - Magnetfeldaenderung', 110),
    ('DeltaI - Stromaenderung bei Selbstinduktion', 111),
    ('DeltaI - Stromaenderung', 112),
    ('DeltaPhi - Aenderung des magnetischen Flusses', 113),
    ('DeltaPhi - Flussaenderung aus Induktionsspannung', 114),
    ('DeltaPhi_phase - Phasenverschiebung im RLC-Kreis', 115),
    ('DeltaPhi_phase - Phasenwinkel aus Zeigerdiagramm', 116),
    ('DeltaPhi_phase - Phasenwinkel aus Leistungsfaktor', 117),
    ('E - elektrische Feldstaerke aus Kraft', 118),
    ('E - homogenes elektrisches Feld', 119),
    ('E0 - Ruheenergie', 120),
    ('E0 - Ruheenergie in eV', 121),
    ('E_cap - Energie im Kondensator', 122),
    ('E_cap - Kondensatorenergie aus Q und U', 123),
    ('E_cap - Kondensatorenergie aus Ladung', 124),
    ('E_kin - kinetische Energie klassisch', 125),
    ('E_kin - kinetische Energie aus Beschleunigungsspannung', 126),
    ('E_kin - kinetische Energie relativistisch', 127),
    ('E_kin - kinetische Energie Mechanik', 128),
    ('E_mag - Energie im Magnetfeld der Spule', 129),
    ('E_mag - Energie im Magnetfeld ueber B,H,V', 130),
    ('E_mag - Energie ueber Leistung-Zeit-Flaeche', 131),
    ('E_pot - potentielle Energie', 132),
    ('E_pot - potentielle Energie aus Energieerhaltung', 133),
    ('F - Newtonsche Kraft', 134),
    ('F - Kraft auf Leiter im Magnetfeld', 135),
    ('F - Kraft zwischen parallelen Leitern', 136),
    ('F_G - Gewichtskraft', 137),
    ('F_G - Gravitationskraft allgemein', 138),
    ('F_L - Lorentzkraft auf Ladung', 139),
    ('F_L - Kraft auf stromdurchflossenen Leiter', 140),
    ('F_R - Reibungskraft', 141),
    ('F_R - Reibungskraft aus Arbeit', 142),
    ('F_el - elektrische Kraft', 143),
    ('F_el - Coulomb-Kraft', 144),
    ('F_r - Radialkraft', 145),
    ('F_r - Radialkraft aus Winkelgeschwindigkeit', 146),
    ('H - Feldstaerke aus B', 147),
    ('H - magnetische Feldstaerke einer Spule', 148),
    ('H - Feldstaerke Ringkern', 149),
    ('I - Strom aus magnetischer Flussdichte einer Spule', 150),
    ('I - Strom aus magnetischer Feldstaerke', 151),
    ('I - Strom aus magnetischem Fluss und Induktivitaet', 152),
    ('I - Strom aus Kraft auf Leiter im Magnetfeld', 153),
    ('I - Strom aus elektrischer Leistung', 154),
    ('I - Strom aus Leistung am Widerstand', 155),
    ('I - Strom aus Wechselstromkreis', 156),
    ('I - Strom aus magnetischer Energie', 157),
    ('I - Stromstaerke nach Ohm', 158),
    ('I - Strom im Ringkern aus Feldstaerke', 159),
    ('I0 - Stromamplitude am Kondensator', 160),
    ('I0 - Stromamplitude aus XL', 161),
    ('I0 - Stromamplitude aus XC', 162),
    ('I1 - Primaerstrom am Transformator', 163),
    ('I1 - Strom paralleler Leiter', 164),
    ('I2 - Sekundaerstrom am Transformator', 165),
    ('I2 - Sekundaerstrom idealer Transformator', 166),
    ('I2 - Strom paralleler Leiter', 167),
    ('I_eff - Effektivstrom', 168),
    ('I_eff - Effektivstrom aus Scheitelwert', 169),
    ('I_eff - Effektivstrom aus Wirkleistung', 170),
    ('L - Induktivitaet aus Spulengeometrie', 171),
    ('L - Induktivitaet aus Selbstinduktion', 172),
    ('L - Induktivitaet aus X_L', 173),
    ('L - Induktivitaet aus Fluss', 174),
    ('N - Windungszahl aus Spulenfeld', 175),
    ('N - Windungszahl aus Feldstaerke', 176),
    ('N - Windungszahl aus Drahtdurchmesser', 177),
    ('N - Windungszahl aus Flussverkettung', 178),
    ('N1 - Primaerwindungen aus Spannung', 179),
    ('N1 - Primaerwindungen aus Stromverhaeltnis', 180),
    ('N2 - Sekundaerwindungszahl', 181),
    ('N2 - Sekundaerwindungen aus Stromverhaeltnis', 182),
    ('P - elektrische Leistung', 183),
    ('P - Leistung am Widerstand', 184),
    ('P - Wirkleistung Wechselstrom', 185),
    ('P_V - Verlustleistung in Leitung', 186),
    ('P_V - Verlustleistung aus Spannung', 187),
    ('P_V - Verlustleistung als Differenz', 188),
    ('Phi - magnetischer Fluss', 189),
    ('Phi - magnetischer Fluss aus Induktivitaet', 190),
    ('Phi - magnetischer Fluss aus B und Flaeche', 191),
    ('Phi_E - elektrischer Fluss', 192),
    ('Phi_E - elektrischer Fluss aus Ladung', 193),
    ('Q - Kondensatorladung', 194),
    ('Q - Ladung aus Strom und Zeit', 195),
    ('Q - Ladung aus Feldfluss', 196),
    ('Q_blind - Blindleistung', 197),
    ('Q_blind - Blindleistung aus S und P', 198),
    ('R - Ohmscher Widerstand', 199),
    ('R - Wirkwiderstand aus Impedanz', 200),
    ('R - Widerstand aus Leistung', 201),
    ('R - Widerstand aus Leistung und Spannung', 202),
    ('R - Drahtwiderstand', 203),
    ('S - Scheinleistung', 204),
    ('S - Scheinleistung aus P und Q', 205),
    ('T - Periodendauer', 206),
    ('T - Thomsonsche Schwingungsdauer', 207),
    ('U - Spannung am Widerstand', 208),
    ('U - Spannung im homogenen E-Feld', 209),
    ('U0 - Spannungsamplitude Kondensator', 210),
    ('U0 - Scheitelspannung aus Effektivwert', 211),
    ('U1 - Primaerspannung Transformator', 212),
    ('U1 - Primaerspannung aus Stromverhaeltnis', 213),
    ('U2 - Sekundaerspannung Transformator', 214),
    ('U2 - Sekundaerspannung aus Stromverhaeltnis', 215),
    ('U_eff - Effektivspannung', 216),
    ('U_eff - Effektivspannung aus Leistung', 217),
    ('U_ind - Induktionsspannung nach Faraday', 218),
    ('U_ind - Induktion durch Feldaenderung', 219),
    ('U_ind - Induktion durch Flaechenaenderung', 220),
    ('U_ind - Bewegungsinduktion am Leiter', 221),
    ('U_ind - Rahmen tritt in Magnetfeld ein/aus', 222),
    ('U_ind - Generator mit sinusfoermigem Feld', 223),
    ('U_ind - Dreieckgenerator / Dreiecksignal', 224),
    ('U_ind - Selbstinduktionsspannung', 225),
    ('U_ind - Bewegungsinduktion mit Winkel', 226),
    ('U_ind - Dreiecksignal Induktion', 227),
    ('U_max - Scheitelspannung', 228),
    ('U_max - Generator Sinus-Spannung', 229),
    ('W - mechanische Arbeit', 230),
    ('W - Arbeit aus Energiedifferenz', 231),
    ('W_el - elektrische Arbeit/Energie', 232),
    ('W_el - elektrische Arbeit aus Leistung', 233),
    ('X_C - kapazitiver Blindwiderstand', 234),
    ('X_C - kapazitiver Widerstand aus Amplituden', 235),
    ('X_L - induktiver Blindwiderstand', 236),
    ('X_L - induktiver Widerstand aus Amplituden', 237),
    ('Z - Impedanz RLC-Reihenschaltung', 238),
    ('Z - Impedanz RL-Reihe', 239),
    ('Z - Impedanz RC-Reihe', 240),
    ('a - Abstand paralleler Leiter', 241),
    ('a - Beschleunigung nach Newton', 242),
    ('a - Beschleunigung aus Geschwindigkeit', 243),
    ('a_r - Radialbeschleunigung', 244),
    ('a_r - Radialbeschleunigung aus T', 245),
    ('beta - Geschwindigkeit relativ zu c', 246),
    ('beta - beta aus gamma', 247),
    ('cos_phi - Leistungsfaktor', 248),
    ('cos_phi - Leistungsfaktor aus Leistung', 249),
    ('d - Durchmesser aus Flaeche', 250),
    ('d - Durchmesser aus Radius', 251),
    ('d - Plattenabstand aus E-Feld', 252),
    ('eps0 - elektrische Feldkonstante', 253),
    ('eps_r - relative Permittivitaet', 254),
    ('eps_r - relative Permittivitaet aus Feldstaerken', 255),
    ('eta - Wirkungsgrad', 256),
    ('eta - Trafo-Wirkungsgrad', 257),
    ('eta - Wirkungsgrad aus Verlustleistung', 258),
    ('f - Frequenz aus Periodendauer', 259),
    ('f - Frequenz aus Sinus-Induktion', 260),
    ('f - Frequenz aus Dreiecksignal', 261),
    ('f0 - Resonanzfrequenz / Eigenfrequenz', 262),
    ('f0 - Resonanzfrequenz aus Periodendauer', 263),
    ('gamma - Lorentzfaktor', 264),
    ('gamma - gamma aus Zeitdilatation', 265),
    ('h - Fallhoehe aus Geschwindigkeit', 266),
    ('h - Hoehe aus Lageenergie', 267),
    ('h - Fallhoehe aus Zeit', 268),
    ('l - Laenge eines Leiters im Magnetfeld', 269),
    ('l - Laenge aus Kraft auf stromdurchflossenen Leiter', 270),
    ('l - Spulenlaenge aus magnetischer Feldstaerke', 271),
    ('l - Spulenlaenge aus magnetischer Flussdichte', 272),
    ('l - Spulenlaenge aus Induktivitaet', 273),
    ('l - Drahtlaenge aus Widerstandsgesetz', 274),
    ('l - Wellenlaenge aus Wellengeschwindigkeit', 275),
    ('l - magnetische Weglaenge im Ringkern', 276),
    ('l_Draht - Drahtlaenge aus Windungszahl und Umfang', 277),
    ('l_Draht - Drahtlaenge aus Widerstandsgesetz', 278),
    ('m - Masse im Massenspektrometer', 279),
    ('m - Masse aus Beschleunigung und Kreisbahn', 280),
    ('mu0 - magnetische Feldkonstante', 281),
    ('mu_r - relative Permeabilitaet aus B', 282),
    ('mu_r - relative Permeabilitaet aus Induktivitaet', 283),
    ('mu_r - relative Permeabilitaet', 284),
    ('omega - Kreisfrequenz', 285),
    ('omega - Kreisfrequenz aus Periodendauer', 286),
    ('omega - Eigenkreisfrequenz LC', 287),
    ('omega - omega aus XL', 288),
    ('omega - omega aus XC', 289),
    ('p - Impuls', 290),
    ('p - Impulsaenderung', 291),
    ('q_m - spezifische Ladung q/m', 292),
    ('q_m - spezifische Ladung aus Kreisbahn', 293),
    ('r - Radius der Kreisbahn im B-Feld', 294),
    ('r - Radius aus Flaeche', 295),
    ('r - mittlerer Radius Ringkern', 296),
    ('rho - spezifischer Widerstand', 297),
    ('rho - spezifischer Widerstand aus U,I', 298),
    ('tau - Zeitkonstante RL-Kreis', 299),
    ('tau - Zeitkonstante RC-Kreis', 300),
    ('v - Teilchengeschwindigkeit aus Kreisbahn', 301),
    ('v - Geschwindigkeit nach Beschleunigungsspannung', 302),
    ('v - Geschwindigkeit aus Fallhoehe', 303),
    ('v - Geschwindigkeit aus Bewegungsinduktion', 304),
    ('v_filter - Geschwindigkeit im Wien-Filter', 305),
    ('v_filter - Filtergeschwindigkeit mit Plattenfeld', 306),
    ('l - Laenge eines Leiters im Magnetfeld', 269),
    ('DeltaPhi - Aenderung des magnetischen Flusses', 113),
    ('DeltaPhi - Flussaenderung aus Induktionsspannung', 114),
    ('U_ind - Induktionsspannung nach Faraday', 218),
    ('U_ind - Induktion durch Feldaenderung', 219),
    ('U_ind - Induktion durch Flaechenaenderung', 220),
    ('U_ind - Bewegungsinduktion am Leiter', 221),
    ('U_ind - Generator mit sinusfoermigem Feld', 223),
    ('U_ind - Dreieckgenerator / Dreiecksignal', 224),
    ('B - magnetische Flussdichte aus Fluss', 98),
    ('P - Leistung am Widerstand', 184),
    ('rho - spezifischer Widerstand', 297),
    ('E0 - Ruheenergie', 120),
    ('A - Kreisflaeche aus Durchmesser', 94),
    ('A - Rechteckflaeche', 95),
    ('Phi - magnetischer Fluss aus B und Flaeche', 191),
    ('U_ind - Bewegungsinduktion mit Winkel', 226),
    ('v - Geschwindigkeit aus Bewegungsinduktion', 304),
    ('B - B aus Bewegungsinduktion', 102),
    ('DeltaB - B-Aenderung aus Induktion', 109),
    ('DeltaA - Flaechenaenderung aus Induktion', 107),
    ('U_max - Generator Sinus-Spannung', 229),
    ('B_max - B-Amplitude aus Generator', 103),
    ('f - Frequenz aus Sinus-Induktion', 260),
    ('U_ind - Dreiecksignal Induktion', 227),
    ('f - Frequenz aus Dreiecksignal', 261),
    ('B_max - B-Amplitude aus Dreiecksignal', 104),
    ('Q - Ladung aus Feldfluss', 196),
    ('Phi_E - elektrischer Fluss aus Ladung', 193),
    ('DeltaA - Flaechenaenderung', 108),
    ('DeltaB - Magnetfeldaenderung', 110),
    ('I - Strom aus magnetischer Flussdichte einer Spule', 150),
    ('I - Strom aus magnetischer Feldstaerke', 151),
    ('I - Strom aus magnetischem Fluss und Induktivitaet', 152),
    ('N - Windungszahl aus Spulenfeld', 175),
    ('N - Windungszahl aus Feldstaerke', 176),
    ('mu_r - relative Permeabilitaet aus B', 282),
    ('mu_r - relative Permeabilitaet aus Induktivitaet', 283),
    ('A - Flaeche aus Induktivitaet', 92),
    ('B - B aus Feldstaerke und Permeabilitaet', 97),
    ('H - Feldstaerke aus B', 147),
    ('l - Spulenlaenge aus magnetischer Feldstaerke', 271),
    ('l - Spulenlaenge aus magnetischer Flussdichte', 272),
    ('l - Spulenlaenge aus Induktivitaet', 273),
    ('l - Drahtlaenge aus Widerstandsgesetz', 274),
    ('Phi - magnetischer Fluss', 189),
    ('Phi - magnetischer Fluss aus Induktivitaet', 190),
    ('B - Magnetfeld einer langen Spule', 99),
    ('H - magnetische Feldstaerke einer Spule', 148),
    ('mu0 - magnetische Feldkonstante', 281),
    ('mu_r - relative Permeabilitaet', 284),
    ('L - Induktivitaet aus Spulengeometrie', 171),
    ('L - Induktivitaet aus Selbstinduktion', 172),
    ('U_ind - Selbstinduktionsspannung', 225),
    ('DeltaI - Stromaenderung bei Selbstinduktion', 111),
    ('E_mag - Energie im Magnetfeld der Spule', 129),
    ('I - Strom aus magnetischer Energie', 157),
    ('tau - Zeitkonstante RL-Kreis', 299),
    ('v - Geschwindigkeit aus Fallhoehe', 303),
    ('A - Kreisflaeche aus Radius', 93),
    ('A - Drahtquerschnitt aus Widerstand', 96),
    ('d - Durchmesser aus Flaeche', 250),
    ('l - magnetische Weglaenge im Ringkern', 276),
    ('r - mittlerer Radius Ringkern', 296),
    ('l_Draht - Drahtlaenge aus Windungszahl und Umfang', 277),
    ('N - Windungszahl aus Drahtdurchmesser', 177),
    ('H - Feldstaerke Ringkern', 149),
    ('I - Strom im Ringkern aus Feldstaerke', 159),
    ('L - Induktivitaet aus Fluss', 174),
    ('N - Windungszahl aus Flussverkettung', 178),
    ('R - Drahtwiderstand', 203),
    ('rho - spezifischer Widerstand aus U,I', 298),
    ('E_mag - Energie im Magnetfeld ueber B,H,V', 130),
    ('E_mag - Energie ueber Leistung-Zeit-Flaeche', 131),
    ('DeltaI - Stromaenderung', 112),
    ('d - Durchmesser aus Radius', 251),
    ('l_Draht - Drahtlaenge aus Widerstandsgesetz', 278),
    ('Phi_E - elektrischer Fluss', 192),
    ('X_C - kapazitiver Blindwiderstand', 234),
    ('C - Kapazitaet aus X_C', 105),
    ('E - elektrische Feldstaerke aus Kraft', 118),
    ('E - homogenes elektrisches Feld', 119),
    ('U - Spannung im homogenen E-Feld', 209),
    ('F_el - elektrische Kraft', 143),
    ('F_el - Coulomb-Kraft', 144),
    ('W_el - elektrische Arbeit/Energie', 232),
    ('C - Kapazitaet Plattenkondensator', 106),
    ('Q - Kondensatorladung', 194),
    ('E_cap - Energie im Kondensator', 122),
    ('eps0 - elektrische Feldkonstante', 253),
    ('eps_r - relative Permittivitaet', 254),
    ('I0 - Stromamplitude am Kondensator', 160),
    ('U0 - Spannungsamplitude Kondensator', 210),
    ('I0 - Stromamplitude aus XC', 162),
    ('Q_blind - Blindleistung', 197),
    ('E_cap - Kondensatorenergie aus Q und U', 123),
    ('E_cap - Kondensatorenergie aus Ladung', 124),
    ('eps_r - relative Permittivitaet aus Feldstaerken', 255),
    ('tau - Zeitkonstante RC-Kreis', 300),
    ('I - Strom aus elektrischer Leistung', 154),
    ('I - Strom aus Wechselstromkreis', 156),
    ('l - Wellenlaenge aus Wellengeschwindigkeit', 275),
    ('R - Ohmscher Widerstand', 199),
    ('U - Spannung am Widerstand', 208),
    ('P - elektrische Leistung', 183),
    ('f - Frequenz aus Periodendauer', 259),
    ('T - Periodendauer', 206),
    ('omega - Kreisfrequenz', 285),
    ('U_eff - Effektivspannung', 216),
    ('U_max - Scheitelspannung', 228),
    ('I_eff - Effektivstrom', 168),
    ('X_L - induktiver Blindwiderstand', 236),
    ('L - Induktivitaet aus X_L', 173),
    ('Z - Impedanz RLC-Reihenschaltung', 238),
    ('DeltaPhi_phase - Phasenverschiebung im RLC-Kreis', 115),
    ('f0 - Resonanzfrequenz / Eigenfrequenz', 262),
    ('T - Thomsonsche Schwingungsdauer', 207),
    ('X_C - kapazitiver Widerstand aus Amplituden', 235),
    ('X_L - induktiver Widerstand aus Amplituden', 237),
    ('I0 - Stromamplitude aus XL', 161),
    ('omega - Kreisfrequenz aus Periodendauer', 286),
    ('omega - Eigenkreisfrequenz LC', 287),
    ('omega - omega aus XL', 288),
    ('omega - omega aus XC', 289),
    ('Z - Impedanz RL-Reihe', 239),
    ('Z - Impedanz RC-Reihe', 240),
    ('R - Wirkwiderstand aus Impedanz', 200),
    ('DeltaPhi_phase - Phasenwinkel aus Zeigerdiagramm', 116),
    ('DeltaPhi_phase - Phasenwinkel aus Leistungsfaktor', 117),
    ('cos_phi - Leistungsfaktor', 248),
    ('P - Wirkleistung Wechselstrom', 185),
    ('S - Scheinleistung', 204),
    ('I_eff - Effektivstrom aus Scheitelwert', 169),
    ('U_eff - Effektivspannung aus Leistung', 217),
    ('I_eff - Effektivstrom aus Wirkleistung', 170),
    ('f0 - Resonanzfrequenz aus Periodendauer', 263),
    ('P_V - Verlustleistung aus Spannung', 187),
    ('R - Widerstand aus Leistung', 201),
    ('R - Widerstand aus Leistung und Spannung', 202),
    ('Q_blind - Blindleistung aus S und P', 198),
    ('S - Scheinleistung aus P und Q', 205),
    ('U0 - Scheitelspannung aus Effektivwert', 211),
    ('cos_phi - Leistungsfaktor aus Leistung', 249),
    ('I1 - Primaerstrom am Transformator', 163),
    ('I2 - Sekundaerstrom am Transformator', 165),
    ('U2 - Sekundaerspannung Transformator', 214),
    ('U1 - Primaerspannung Transformator', 212),
    ('N2 - Sekundaerwindungszahl', 181),
    ('I2 - Sekundaerstrom idealer Transformator', 166),
    ('eta - Wirkungsgrad', 256),
    ('P_V - Verlustleistung in Leitung', 186),
    ('U2 - Sekundaerspannung aus Stromverhaeltnis', 215),
    ('U1 - Primaerspannung aus Stromverhaeltnis', 213),
    ('N1 - Primaerwindungen aus Spannung', 179),
    ('eta - Trafo-Wirkungsgrad', 257),
    ('eta - Wirkungsgrad aus Verlustleistung', 258),
    ('P_V - Verlustleistung als Differenz', 188),
    ('N1 - Primaerwindungen aus Stromverhaeltnis', 180),
    ('N2 - Sekundaerwindungen aus Stromverhaeltnis', 182),
    ('B - B aus Lorentzkraft auf Ladung', 100),
    ('F_L - Lorentzkraft auf Ladung', 139),
    ('v - Teilchengeschwindigkeit aus Kreisbahn', 301),
    ('q_m - spezifische Ladung q/m', 292),
    ('q_m - spezifische Ladung aus Kreisbahn', 293),
    ('v_filter - Geschwindigkeit im Wien-Filter', 305),
    ('E_kin - kinetische Energie aus Beschleunigungsspannung', 126),
    ('Q - Ladung aus Strom und Zeit', 195),
    ('W_el - elektrische Arbeit aus Leistung', 233),
    ('d - Plattenabstand aus E-Feld', 252),
    ('v_filter - Filtergeschwindigkeit mit Plattenfeld', 306),
    ('I - Strom aus Kraft auf Leiter im Magnetfeld', 153),
    ('l - Laenge aus Kraft auf stromdurchflossenen Leiter', 270),
    ('U_ind - Rahmen tritt in Magnetfeld ein/aus', 222),
    ('B - B aus Kraft auf stromdurchflossenen Leiter', 101),
    ('F_L - Kraft auf stromdurchflossenen Leiter', 140),
    ('r - Radius der Kreisbahn im B-Feld', 294),
    ('v - Geschwindigkeit nach Beschleunigungsspannung', 302),
    ('m - Masse im Massenspektrometer', 279),
    ('m - Masse aus Beschleunigung und Kreisbahn', 280),
    ('E_kin - kinetische Energie klassisch', 125),
    ('gamma - Lorentzfaktor', 264),
    ('E_kin - kinetische Energie relativistisch', 127),
    ('r - Radius aus Flaeche', 295),
    ('F - Kraft auf Leiter im Magnetfeld', 135),
    ('F - Kraft zwischen parallelen Leitern', 136),
    ('I1 - Strom paralleler Leiter', 164),
    ('I2 - Strom paralleler Leiter', 167),
    ('a - Abstand paralleler Leiter', 241),
    ('beta - beta aus gamma', 247),
    ('h - Fallhoehe aus Geschwindigkeit', 266),
    ('E_kin - kinetische Energie Mechanik', 128),
    ('E_pot - potentielle Energie', 132),
    ('W - mechanische Arbeit', 230),
    ('F - Newtonsche Kraft', 134),
    ('F_G - Gewichtskraft', 137),
    ('F_R - Reibungskraft', 141),
    ('p - Impuls', 290),
    ('a_r - Radialbeschleunigung', 244),
    ('F_r - Radialkraft', 145),
    ('E_pot - potentielle Energie aus Energieerhaltung', 133),
    ('W - Arbeit aus Energiedifferenz', 231),
    ('p - Impulsaenderung', 291),
    ('a_r - Radialbeschleunigung aus T', 245),
    ('F_r - Radialkraft aus Winkelgeschwindigkeit', 146),
    ('F_G - Gravitationskraft allgemein', 138),
    ('F_R - Reibungskraft aus Arbeit', 142),
    ('a - Beschleunigung nach Newton', 242),
    ('a - Beschleunigung aus Geschwindigkeit', 243),
    ('h - Hoehe aus Lageenergie', 267),
    ('h - Fallhoehe aus Zeit', 268),
    ('beta - Geschwindigkeit relativ zu c', 246),
    ('gamma - gamma aus Zeitdilatation', 265),
    ('E0 - Ruheenergie in eV', 121),
    ('I - Strom aus Leistung am Widerstand', 155),
    ('I - Stromstaerke nach Ohm', 158),
]

CHAPTERS = [
    (0, 568),
    (568, 1077),
    (1645, 741),
    (2386, 771),
    (3157, 686),
    (3843, 626),
    (4469, 669),
    (5138, 372),
    (5510, 577),
    (6087, 597),
    (6684, 520),
    (7204, 663),
    (7867, 455),
    (8322, 477),
    (8799, 640),
    (9439, 603),
    (10042, 677),
    (10719, 608),
    (11327, 649),
    (11976, 671),
    (12647, 766),
    (13413, 495),
    (13908, 503),
    (14411, 675),
    (15086, 623),
    (15709, 748),
    (16457, 908),
    (17365, 426),
    (17791, 423),
    (18214, 319),
    (18533, 391),
    (18924, 341),
    (19265, 311),
    (19576, 301),
    (19877, 410),
    (20287, 269),
    (20556, 342),
    (20898, 383),
    (21281, 334),
    (21615, 340),
    (21955, 324),
    (22279, 308),
    (22587, 312),
    (22899, 334),
    (23233, 297),
    (23530, 324),
    (23854, 310),
    (24164, 320),
    (24484, 363),
    (24847, 307),
    (25154, 252),
    (25406, 307),
    (25713, 277),
    (25990, 273),
    (26263, 274),
    (26537, 224),
    (26761, 202),
    (26963, 215),
    (27178, 234),
    (27412, 236),
    (27648, 207),
    (27855, 227),
    (28082, 218),
    (28300, 255),
    (28555, 232),
    (28787, 232),
    (29019, 261),
    (29280, 237),
    (29517, 273),
    (29790, 282),
    (30072, 282),
    (30354, 269),
    (30623, 324),
    (30947, 347),
    (31294, 268),
    (31562, 293),
    (31855, 354),
    (32209, 293),
    (32502, 307),
    (32809, 285),
    (33094, 313),
    (33407, 285),
    (33692, 299),
    (33991, 285),
    (34276, 321),
    (34597, 311),
    (34908, 314),
    (35222, 345),
    (35567, 325),
    (35892, 246),
    (36138, 255),
    (36393, 225),
    (36618, 334),
    (36952, 239),
    (37191, 255),
    (37446, 251),
    (37697, 272),
    (37969, 276),
    (38245, 295),
    (38540, 324),
    (38864, 290),
    (39154, 302),
    (39456, 267),
    (39723, 283),
    (40006, 267),
    (40273, 255),
    (40528, 274),
    (40802, 294),
    (41096, 229),
    (41325, 266),
    (41591, 234),
    (41825, 331),
    (42156, 213),
    (42369, 306),
    (42675, 361),
    (43036, 345),
    (43381, 304),
    (43685, 278),
    (43963, 269),
    (44232, 250),
    (44482, 184),
    (44666, 222),
    (44888, 274),
    (45162, 264),
    (45426, 245),
    (45671, 314),
    (45985, 291),
    (46276, 335),
    (46611, 218),
    (46829, 292),
    (47121, 276),
    (47397, 297),
    (47694, 236),
    (47930, 272),
    (48202, 191),
    (48393, 286),
    (48679, 318),
    (48997, 195),
    (49192, 272),
    (49464, 264),
    (49728, 262),
    (49990, 198),
    (50188, 243),
    (50431, 255),
    (50686, 255),
    (50941, 266),
    (51207, 245),
    (51452, 228),
    (51680, 283),
    (51963, 246),
    (52209, 392),
    (52601, 284),
    (52885, 326),
    (53211, 347),
    (53558, 263),
    (53821, 264),
    (54085, 302),
    (54387, 281),
    (54668, 211),
    (54879, 266),
    (55145, 273),
    (55418, 241),
    (55659, 242),
    (55901, 266),
    (56167, 279),
    (56446, 296),
    (56742, 271),
    (57013, 282),
    (57295, 261),
    (57556, 252),
    (57808, 261),
    (58069, 275),
    (58344, 317),
    (58661, 246),
    (58907, 233),
    (59140, 305),
    (59445, 254),
    (59699, 292),
    (59991, 240),
    (60231, 241),
    (60472, 242),
    (60714, 270),
    (60984, 284),
    (61268, 248),
    (61516, 303),
    (61819, 256),
    (62075, 313),
    (62388, 249),
    (62637, 246),
    (62883, 342),
    (63225, 302),
    (63527, 271),
    (63798, 357),
    (64155, 257),
    (64412, 224),
    (64636, 225),
    (64861, 250),
    (65111, 274),
    (65385, 268),
    (65653, 255),
    (65908, 269),
    (66177, 238),
    (66415, 234),
    (66649, 204),
    (66853, 242),
    (67095, 262),
    (67357, 210),
    (67567, 262),
    (67829, 213),
    (68042, 243),
    (68285, 255),
    (68540, 257),
    (68797, 245),
    (69042, 239),
    (69281, 273),
    (69554, 243),
    (69797, 256),
    (70053, 244),
    (70297, 296),
    (70593, 341),
    (70934, 339),
    (71273, 300),
    (71573, 336),
    (71909, 373),
    (72282, 365),
    (72647, 288),
    (72935, 316),
    (73251, 337),
    (73588, 261),
    (73849, 301),
    (74150, 232),
    (74382, 221),
    (74603, 318),
    (74921, 236),
    (75157, 282),
    (75439, 271),
    (75710, 265),
    (75975, 251),
    (76226, 287),
    (76513, 237),
    (76750, 230),
    (76980, 273),
    (77253, 233),
    (77486, 233),
    (77719, 276),
    (77995, 232),
    (78227, 261),
    (78488, 217),
    (78705, 241),
    (78946, 290),
    (79236, 244),
    (79480, 195),
    (79675, 236),
    (79911, 229),
    (80140, 247),
    (80387, 277),
    (80664, 256),
    (80920, 246),
    (81166, 256),
    (81422, 214),
    (81636, 298),
    (81934, 266),
    (82200, 317),
    (82517, 247),
    (82764, 250),
    (83014, 230),
    (83244, 202),
    (83446, 240),
    (83686, 203),
    (83889, 397),
    (84286, 404),
    (84690, 329),
    (85019, 386),
    (85405, 359),
    (85764, 367),
    (86131, 310),
    (86441, 243),
    (86684, 309),
    (86993, 268),
    (87261, 312),
    (87573, 307),
    (87880, 298),
    (88178, 329),
    (88507, 331),
    (88838, 322),
    (89160, 248),
    (89408, 228),
    (89636, 250),
    (89886, 217),
    (90103, 227),
    (90330, 190),
    (90520, 209),
    (90729, 288),
    (91017, 280),
    (91297, 326),
    (91623, 236),
    (91859, 260),
    (92119, 326),
    (92445, 265),
    (92710, 296),
    (93006, 254),
    (93260, 302),
    (93562, 361),
    (93923, 276),
    (94199, 265),
    (94464, 330),
    (94794, 272),
]

import gc
import time

SCREEN_W = 320
SCREEN_H = 528
HEADER_H = 42
ROW_H = 48
VISIBLE_ROWS = (SCREEN_H - HEADER_H) // ROW_H

BG = C_RGB(29, 31, 29)
FG = C_RGB(2, 6, 3)
DIM = C_RGB(10, 14, 10)
ACCENT = C_RGB(4, 18, 12)
SELECTED = C_RGB(20, 26, 20)

KNOWLEDGE_FILE = "wissen.txt"
KNOWLEDGE_PATH = None
SKIP_BLOCK = 512
DEBUG = False


def memory_free():
    try:
        return gc.mem_free()
    except AttributeError:
        return -1


def knowledge_paths():
    """Ermittelt den Ordner der gestarteten physchem_final.py."""
    paths = []
    source_path = globals().get("__file__", "")
    slash = max(source_path.rfind("/"), source_path.rfind("\\"))
    if slash >= 0:
        paths.append(source_path[:slash + 1] + KNOWLEDGE_FILE)
    paths.append("Python/" + KNOWLEDGE_FILE)
    paths.append("/Python/" + KNOWLEDGE_FILE)
    paths.append(KNOWLEDGE_FILE)
    return paths


def open_knowledge():
    global KNOWLEDGE_PATH
    if KNOWLEDGE_PATH is not None:
        return open(KNOWLEDGE_PATH, "rb")
    for path in knowledge_paths():
        try:
            handle = open(path, "rb")
            KNOWLEDGE_PATH = path
            if DEBUG:
                print("[DEBUG] Wissen gefunden, funktionier du drecks app", path)
            return handle
        except OSError:
            pass
    raise OSError("wissen.txt fehlt neben physchem_final.py")


def load_chapter(chapter_id):
    start, length = CHAPTERS[chapter_id]
    if DEBUG:
        print("[DEBUG] Kapitel laden. Lade oder ich finde dich du hs:", chapter_id)
    handle = open_knowledge()
    try:
        remaining = start
        blocks_since_gc = 0
        # Kein seek(): PythonExtra macht bei grossen offsets sonst wieder einen auf Hartzer und macht nichts.
        while remaining > 0:
            block_size = min(SKIP_BLOCK, remaining)
            skipped = handle.read(block_size)
            if len(skipped) != block_size:
                raise OSError("Byteposition ausserhalb von wissen.txt")
            remaining -= block_size
            del skipped
            blocks_since_gc += 1
            if blocks_since_gc == 16:
                # Der winzige Heap ist ein Stück scheiße.
                gc.collect()
                blocks_since_gc = 0
        data = handle.read(length)
    finally:
        handle.close()
    if len(data) != length:
        raise OSError("Kapitel unvollstaendig")
    if isinstance(data, str):
        return data
    text = data.decode("ascii")
    # Bytes sofort loswerden. Der kleine Speicher fickt mich sonst schonwieder.
    del data
    return text


def wrap_text(text, width):
    lines = []
    for raw in text.split("\n"):
        if raw == "":
            lines.append("")
            continue
        #ich habe gesagt lade du Hurrensohnasföuhaseöuigfb
        line = ""
        for word in raw.split(" "):
            if line == "":
                line = word
            elif len(line) + len(word) + 1 <= width:
                line += " " + word
            else:
                lines.append(line)
                line = word
        if line:
            lines.append(line)
    return lines


def poll_events():
    events = []
    event = pollevent()
    while event.type != KEYEV_NONE:
        events.append(event)
        event = pollevent()
    return events


def draw_header(title, back):
    drect(0, 0, SCREEN_W, HEADER_H, ACCENT)
    if back:
        dline(12, 21, 24, 10, C_WHITE)
        dline(12, 21, 24, 32, C_WHITE)
        dline(12, 21, 34, 21, C_WHITE)
    if len(title) > 30:
        title = title[:27] + "..."
    dtext_opt(
        SCREEN_W // 2,
        HEADER_H // 2,
        C_WHITE,
        C_NONE,
        DTEXT_CENTER,
        DTEXT_MIDDLE,
        title,
        -1,
    )


def list_rows(source, start, count):
    rows = []
    index = start
    end = start + count
    while index < end:
        rows.append(source[index])
        index += 1
    return rows


def draw_list(title, rows, selected, back):
    dclear(BG)
    first = max(0, min(selected - VISIBLE_ROWS // 2, len(rows) - VISIBLE_ROWS))
    last = min(len(rows), first + VISIBLE_ROWS)
    y = HEADER_H
    index = first
    while index < last:
        text = rows[index][0]
        color = SELECTED if index == selected else BG
        drect(0, y, SCREEN_W, y + ROW_H, color)
        dline(0, y + ROW_H, SCREEN_W, y + ROW_H, DIM)
        if len(text) > 35:
            text = text[:32] + "..."
        dtext_opt(12, y + ROW_H // 2, FG, C_NONE, DTEXT_LEFT, DTEXT_MIDDLE, text, -1)
        dtext_opt(303, y + ROW_H // 2, DIM, C_NONE, DTEXT_CENTER, DTEXT_MIDDLE, ">", -1)
        y += ROW_H
        index += 1
    draw_header(title, back)


def select_list(title, rows, back):
    selected = 0
    running = True
    while running:
        draw_list(title, rows, selected, back)
        dupdate()
        cleareventflips()
        events = poll_events()
        if keypressed(KEY_DEL):
            return None
        for event in events:
            if event.type == KEYEV_DOWN:
                if event.key == KEY_UP:
                    selected = max(0, selected - 1)
                elif event.key == KEY_DOWN:
                    selected = min(len(rows) - 1, selected + 1)
                elif event.key == KEY_EXE:
                    return selected
                elif event.key in (KEY_DEL, KEY_EXIT):
                    return None
            elif event.type == KEYEV_TOUCH_UP:
                if back and event.y < HEADER_H and event.x < 70:
                    return None
                first = max(0, min(selected - VISIBLE_ROWS // 2, len(rows) - VISIBLE_ROWS))
                row = (event.y - HEADER_H) // ROW_H
                touched = first + row
                if 0 <= row < VISIBLE_ROWS and touched < len(rows):
                    return touched
        time.sleep(0.01)
    return None


def show_article(title, chapter_id):
    before = memory_free()
    text = load_chapter(chapter_id)
    after_load = memory_free()
    lines = wrap_text(text, 39)
    after_wrap = memory_free()
    scroll = 0
    max_scroll = max(0, len(lines) * 18 - (SCREEN_H - HEADER_H - 12))
    running = True

    while running:
        dclear(BG)
        y = HEADER_H + 8 - scroll
        for line in lines:
            if y > HEADER_H - 18 and y < SCREEN_H:
                dtext_opt(8, y, FG, C_NONE, DTEXT_LEFT, DTEXT_TOP, line, -1)
            y += 18
        draw_header(title, True)
        dupdate()
        cleareventflips()

        events = poll_events()
        if keypressed(KEY_DEL):
            running = False
        for event in events:
            if event.type == KEYEV_DOWN:
                if event.key == KEY_UP:
                    scroll = max(0, scroll - 18)
                elif event.key == KEY_DOWN:
                    scroll = min(max_scroll, scroll + 18)
                elif event.key in (KEY_DEL, KEY_EXIT):
                    running = False
            elif event.type == KEYEV_TOUCH_UP:
                if event.y < HEADER_H and event.x < 70:
                    running = False
        time.sleep(0.01)

    # Nach dem Regen kommt der Donner
    del lines
    del text
    gc.collect()
    if DEBUG:
        print("[DEBUG] Artikel geschlossen......")
    return before, after_load, after_wrap, memory_free()


def show_memory(result):
    labels = ("vorher", "geladen", "umgebrochen", "freigegeben")
    running = True
    while running:
        dclear(BG)
        draw_header("RAM-Messung", True)
        y = HEADER_H + 35
        index = 0
        while index < len(labels):
            dtext_opt(
                14,
                y,
                FG,
                C_NONE,
                DTEXT_LEFT,
                DTEXT_TOP,
                labels[index] + ": " + str(result[index]),
                -1,
            )
            y += 38
            index += 1
        dtext_opt(14, y + 20, DIM, C_NONE, DTEXT_LEFT, DTEXT_TOP, "DEL: zurueck", -1)
        dupdate()
        cleareventflips()
        events = poll_events()
        if keypressed(KEY_DEL):
            running = False
        for event in events:
            if event.type == KEYEV_DOWN and event.key in (KEY_DEL, KEY_EXIT, KEY_EXE):
                running = False
            elif event.type == KEYEV_TOUCH_UP and event.y < HEADER_H and event.x < 70:
                running = False
        time.sleep(0.01)


def run():
    while True:
        mode_index = select_list("Physik LK On-Demand", MODES, False)
        if mode_index is None:
            return
        mode_title, section_start, section_count = MODES[mode_index]
        sections = list_rows(SECTIONS, section_start, section_count)
        section_index = select_list(mode_title, sections, True)
        while section_index is not None:
            section_title, entry_start, entry_count = sections[section_index]
            entries = list_rows(ENTRIES, entry_start, entry_count)
            entry_index = select_list(section_title, entries, True)
            while entry_index is not None:
                title, chapter_id = entries[entry_index]
                result = show_article(title, chapter_id)
                show_memory(result)
                entry_index = select_list(section_title, entries, True)
            section_index = select_list(mode_title, sections, True)


run()
