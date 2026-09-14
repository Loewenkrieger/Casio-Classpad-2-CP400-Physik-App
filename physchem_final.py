"""Physik-LK-App mit Wissen, das per Byteindex aus wissen.txt geladen wird."""

from gint import *
# Automatisch aus physchem-final.py erzeugter Byteindex.

MODES = [
    ('Theorie', 0, 21),
    ('Formeln nach Groessen', 21, 82),
    ('Formeln nach Themen', 103, 12),
]

SECTIONS = [
    ('Ueberblick', 0, 1),
    ('Mechanik', 1, 1),
    ('Mechanische Schwingungen', 2, 7),
    ('Elektrisches Feld', 9, 1),
    ('Magnetfeld / Teilchen', 10, 4),
    ('Induktion', 14, 3),
    ('Lenz / Wirbelstroeme', 17, 2),
    ('Spule / Trafo', 19, 3),
    ('Wechselstrom / RLC', 22, 8),
    ('Elektrische Schwingungen', 30, 6),
    ('Konzepte / Relativitaet', 36, 1),
    ('Praktikum / Einheiten', 37, 2),
    ('Lehrer-Material', 39, 1),
    ('Lexikon: Konstanten / Material', 40, 10),
    ('Lexikon: Induktion / Spule', 50, 8),
    ('Lexikon: Wechselstrom / RLC', 58, 14),
    ('Lexikon: Mechanik', 72, 13),
    ('Lexikon: Felder Basis', 85, 5),
    ('Lexikon: Teilchen erweitert', 90, 8),
    ('Lexikon: Lehrer-Material', 98, 8),
    ('Lexikon: WSK-Folien', 106, 8),
    ('A', 114, 5),
    ('A_s', 119, 2),
    ('B', 121, 6),
    ('B_max', 127, 2),
    ('C', 129, 4),
    ('DeltaA', 133, 2),
    ('DeltaB', 135, 2),
    ('DeltaI', 137, 2),
    ('DeltaPhi', 139, 2),
    ('DeltaPhi_phase', 141, 3),
    ('E', 144, 2),
    ('E0', 146, 2),
    ('E_cap', 148, 3),
    ('E_kin', 151, 4),
    ('E_mag', 155, 3),
    ('E_pot', 158, 2),
    ('F', 160, 3),
    ('F_G', 163, 2),
    ('F_L', 165, 2),
    ('F_R', 167, 2),
    ('F_el', 169, 2),
    ('F_r', 171, 2),
    ('H', 173, 3),
    ('I', 176, 10),
    ('I0', 186, 3),
    ('I1', 189, 2),
    ('I2', 191, 3),
    ('I_eff', 194, 3),
    ('L', 197, 6),
    ('N', 203, 4),
    ('N1', 207, 2),
    ('N2', 209, 2),
    ('P', 211, 4),
    ('P_V', 215, 3),
    ('Phi', 218, 3),
    ('Phi_E', 221, 2),
    ('Q', 223, 3),
    ('Q_blind', 226, 5),
    ('R', 231, 6),
    ('S', 237, 2),
    ('T', 239, 5),
    ('U', 244, 2),
    ('U0', 246, 2),
    ('U1', 248, 2),
    ('U2', 250, 2),
    ('U_eff', 252, 3),
    ('U_ind', 255, 10),
    ('U_max', 265, 2),
    ('W', 267, 2),
    ('W_el', 269, 2),
    ('X_C', 271, 2),
    ('X_L', 273, 2),
    ('Z', 275, 3),
    ('a', 278, 3),
    ('a_max', 281, 1),
    ('a_r', 282, 2),
    ('beta', 284, 2),
    ('cos_phi', 286, 3),
    ('d', 289, 3),
    ('eps0', 292, 1),
    ('eps_r', 293, 2),
    ('eta', 295, 3),
    ('f', 298, 6),
    ('f0', 304, 2),
    ('g', 306, 1),
    ('gamma', 307, 2),
    ('h', 309, 3),
    ('l', 312, 8),
    ('l_Draht', 320, 2),
    ('m', 322, 2),
    ('mu0', 324, 1),
    ('mu_r', 325, 3),
    ('omega', 328, 7),
    ('p', 335, 2),
    ('q_m', 337, 2),
    ('r', 339, 3),
    ('rho', 342, 2),
    ('sin_phi', 344, 1),
    ('tau', 345, 2),
    ('v', 347, 4),
    ('v_max', 351, 1),
    ('v_filter', 352, 2),
    ('Induktion / Fluss', 354, 31),
    ('Spule / Selbstinduktion', 385, 46),
    ('Kondensator', 431, 22),
    ('Wechselstrom / RLC', 453, 57),
    ('Schwingungen Elektrisch', 510, 20),
    ('Transformator', 530, 16),
    ('Elektrisches Feld', 546, 11),
    ('Magnetfeld / Teilchen', 557, 19),
    ('Schwingungen Mechanik', 576, 26),
    ('Mechanik', 602, 21),
    ('Relativitaet', 623, 3),
    ('Sonstige', 626, 2),
]

ENTRIES = [
    ('Sachsen LK 11 Ueberblick', 0),
    ('Mechanik komplett', 1),
    ('Schwingung Grundidee', 2),
    ('Harmonische Schwingung', 3),
    ('Federpendel', 4),
    ('Fadenpendel', 5),
    ('Energie der Schwingung', 6),
    ('Daempfung und Resonanz', 7),
    ('Mechanisch-elektrische Analogie', 8),
    ('Elektrisches Feld / Kondensator', 9),
    ('Magnetfeld / geladene Teilchen', 10),
    ('Teilchenbeschleuniger', 11),
    ('Elektron im B-Feld', 12),
    ('Massenspektrometer / Filter', 13),
    ('Induktion / magnetischer Fluss', 14),
    ('IQB Parameter A-F', 15),
    ('Induktion mit Ableitungen', 16),
    ('Lenzsche Regel / Wirbelstroeme', 17),
    ('Wirbelstroeme Anwendungen', 18),
    ('Selbstinduktion / Spule', 19),
    ('Transformator', 20),
    ('Transformator erweitert', 21),
    ('Ohmsches Bauelement im WSK', 22),
    ('Kondensator im WSK', 23),
    ('Spule im WSK', 24),
    ('Wirk- und Blindwiderstand', 25),
    ('Zeigerdiagramm', 26),
    ('RLC-Reihenschaltung / Siebkreis', 27),
    ('Resonanz / Thomson', 28),
    ('Energieumwandlung im RLC', 29),
    ('LC-Schwingkreis Grundidee', 30),
    ('Ladung Strom Spannung', 31),
    ('Energie im LC-Kreis', 32),
    ('RLC und Daempfung', 33),
    ('Resonanz im Stromkreis', 34),
    ('Guete und Bandbreite', 35),
    ('Elektromagnetismus-Konzepte', 36),
    ('Praktikum / Messunsicherheiten', 37),
    ('Einheitenwissen / typische Fehler', 38),
    ('Lehrer-Material Ueberblick', 39),
    ('mu0 - magnetische Feldkonstante', 40),
    ('mu_r - relative Permeabilitaet', 41),
    ('H - magnetische Feldstaerke', 42),
    ('B - magnetische Flussdichte', 43),
    ('Phi - magnetischer Fluss', 44),
    ('eps0 - elektrische Feldkonstante', 45),
    ('eps_r - relative Permittivitaet', 46),
    ('rho - spezifischer elektrischer Widerstand', 47),
    ('e - Elementarladung', 48),
    ('c - Lichtgeschwindigkeit', 49),
    ('U_ind - Induktionsspannung', 50),
    ('N - Windungszahl', 51),
    ('A - wirksame Flaeche', 52),
    ('alpha - Winkel', 53),
    ('Delta Phi - Flussaenderung', 54),
    ('dPhi/dt - momentane Flussaenderungsrate', 55),
    ('L - Induktivitaet', 56),
    ('E_mag - magnetische Energie', 57),
    ('R - ohmscher Wirkwiderstand', 58),
    ('X_L - induktiver Blindwiderstand', 59),
    ('X_C - kapazitiver Blindwiderstand', 60),
    ('Z - Impedanz / Scheinwiderstand', 61),
    ('Delta phi - Phasenverschiebung', 62),
    ('omega - Kreisfrequenz', 63),
    ('f0 - Resonanzfrequenz', 64),
    ('T - Periodendauer / Schwingungsdauer', 65),
    ('U_eff - Effektivspannung', 66),
    ('I_eff - Effektivstrom', 67),
    ('q - Schwingkreisladung', 68),
    ('I0 - Stromamplitude', 69),
    ('U_C - Kondensatorspannung', 70),
    ('Q - Guete', 71),
    ('E_kin - Bewegungsenergie', 72),
    ('E_pot - Lageenergie', 73),
    ('E_sp - Spannenergie', 74),
    ('W - Arbeit', 75),
    ('P - Leistung', 76),
    ('p - Impuls', 77),
    ('F - Kraft', 78),
    ('a - Beschleunigung', 79),
    ('A_s - Amplitude', 80),
    ('D - Federkonstante', 81),
    ('x - Auslenkung', 82),
    ('omega0 - Eigenkreisfrequenz', 83),
    ('phi0 - Anfangsphase', 84),
    ('E - elektrische Feldstaerke', 85),
    ('q - elektrische Ladung', 86),
    ('C - Kapazitaet', 87),
    ('F_L - Lorentzkraft', 88),
    ('r - Kreisbahnradius', 89),
    ('q - Ladung', 90),
    ('m - Masse', 91),
    ('q/m - spezifische Ladung', 92),
    ('r - Kreisbahnradius', 93),
    ('v - Teilchengeschwindigkeit', 94),
    ('E_kin - kinetische Energie', 95),
    ('gamma - Lorentzfaktor', 96),
    ('U_B - Beschleunigungsspannung', 97),
    ('q/m - spezifische Ladung', 98),
    ('v_filter - Filtergeschwindigkeit', 99),
    ('rho - spezifischer Widerstand', 100),
    ('H - magnetische Feldstaerke', 101),
    ('mu_r - relative Permeabilitaet', 102),
    ('P_V - Verlustleistung', 103),
    ('gamma - Lorentzfaktor', 104),
    ('E_kin - kinetische Energie geladener Teilchen', 105),
    ('R - ohmscher Wirkwiderstand', 106),
    ('X_L - induktiver Blindwiderstand', 107),
    ('X_C - kapazitiver Blindwiderstand', 108),
    ('Z - Impedanz / Scheinwiderstand', 109),
    ('Delta phi - Phasenverschiebung', 110),
    ('f0 - Resonanzfrequenz', 111),
    ('T - Schwingungsdauer', 112),
    ('omega - Kreisfrequenz', 113),
    ('A - Flaeche aus Induktivitaet', 114),
    ('A - Kreisflaeche aus Radius', 115),
    ('A - Kreisflaeche aus Durchmesser', 116),
    ('A - Rechteckflaeche', 117),
    ('A - Drahtquerschnitt aus Widerstand', 118),
    ('A_s - Amplitude aus Maximalgeschwindigkeit', 119),
    ('A_s - Amplitude aus Maximalbeschleunigung', 120),
    ('B - B aus Feldstaerke und Permeabilitaet', 121),
    ('B - magnetische Flussdichte aus Fluss', 122),
    ('B - Magnetfeld einer langen Spule', 123),
    ('B - B aus Lorentzkraft auf Ladung', 124),
    ('B - B aus Kraft auf stromdurchflossenen Leiter', 125),
    ('B - B aus Bewegungsinduktion', 126),
    ('B_max - B-Amplitude aus Generator', 127),
    ('B_max - B-Amplitude aus Dreiecksignal', 128),
    ('C - Kapazitaet aus X_C', 129),
    ('C - Kapazitaet aus Thomsonformel', 130),
    ('C - Kapazitaet aus Eigenkreisfrequenz', 131),
    ('C - Kapazitaet Plattenkondensator', 132),
    ('DeltaA - Flaechenaenderung aus Induktion', 133),
    ('DeltaA - Flaechenaenderung', 134),
    ('DeltaB - B-Aenderung aus Induktion', 135),
    ('DeltaB - Magnetfeldaenderung', 136),
    ('DeltaI - Stromaenderung bei Selbstinduktion', 137),
    ('DeltaI - Stromaenderung', 138),
    ('DeltaPhi - Aenderung des magnetischen Flusses', 139),
    ('DeltaPhi - Flussaenderung aus Induktionsspannung', 140),
    ('DeltaPhi_phase - Phasenverschiebung im RLC-Kreis', 141),
    ('DeltaPhi_phase - Phasenwinkel aus Zeigerdiagramm', 142),
    ('DeltaPhi_phase - Phasenwinkel aus Leistungsfaktor', 143),
    ('E - elektrische Feldstaerke aus Kraft', 144),
    ('E - homogenes elektrisches Feld', 145),
    ('E0 - Ruheenergie', 146),
    ('E0 - Ruheenergie in eV', 147),
    ('E_cap - Energie im Kondensator', 148),
    ('E_cap - Kondensatorenergie aus Q und U', 149),
    ('E_cap - Kondensatorenergie aus Ladung', 150),
    ('E_kin - kinetische Energie klassisch', 151),
    ('E_kin - kinetische Energie aus Beschleunigungsspannung', 152),
    ('E_kin - kinetische Energie relativistisch', 153),
    ('E_kin - kinetische Energie Mechanik', 154),
    ('E_mag - Energie im Magnetfeld der Spule', 155),
    ('E_mag - Energie im Magnetfeld ueber B,H,V', 156),
    ('E_mag - Energie ueber Leistung-Zeit-Flaeche', 157),
    ('E_pot - potentielle Energie', 158),
    ('E_pot - potentielle Energie aus Energieerhaltung', 159),
    ('F - Newtonsche Kraft', 160),
    ('F - Kraft auf Leiter im Magnetfeld', 161),
    ('F - Kraft zwischen parallelen Leitern', 162),
    ('F_G - Gewichtskraft', 163),
    ('F_G - Gravitationskraft allgemein', 164),
    ('F_L - Lorentzkraft auf Ladung', 165),
    ('F_L - Kraft auf stromdurchflossenen Leiter', 166),
    ('F_R - Reibungskraft', 167),
    ('F_R - Reibungskraft aus Arbeit', 168),
    ('F_el - elektrische Kraft', 169),
    ('F_el - Coulomb-Kraft', 170),
    ('F_r - Radialkraft', 171),
    ('F_r - Radialkraft aus Winkelgeschwindigkeit', 172),
    ('H - Feldstaerke aus B', 173),
    ('H - magnetische Feldstaerke einer Spule', 174),
    ('H - Feldstaerke Ringkern', 175),
    ('I - Strom aus magnetischer Flussdichte einer Spule', 176),
    ('I - Strom aus magnetischer Feldstaerke', 177),
    ('I - Strom aus magnetischem Fluss und Induktivitaet', 178),
    ('I - Strom aus Kraft auf Leiter im Magnetfeld', 179),
    ('I - Strom aus elektrischer Leistung', 180),
    ('I - Strom aus Leistung am Widerstand', 181),
    ('I - Strom aus Wechselstromkreis', 182),
    ('I - Strom aus magnetischer Energie', 183),
    ('I - Stromstaerke nach Ohm', 184),
    ('I - Strom im Ringkern aus Feldstaerke', 185),
    ('I0 - Stromamplitude am Kondensator', 186),
    ('I0 - Stromamplitude aus XL', 187),
    ('I0 - Stromamplitude aus XC', 188),
    ('I1 - Primaerstrom am Transformator', 189),
    ('I1 - Strom paralleler Leiter', 190),
    ('I2 - Sekundaerstrom am Transformator', 191),
    ('I2 - Sekundaerstrom idealer Transformator', 192),
    ('I2 - Strom paralleler Leiter', 193),
    ('I_eff - Effektivstrom', 194),
    ('I_eff - Effektivstrom aus Scheitelwert', 195),
    ('I_eff - Effektivstrom aus Wirkleistung', 196),
    ('L - Induktivitaet aus Spulengeometrie', 197),
    ('L - Induktivitaet aus Selbstinduktion', 198),
    ('L - Induktivitaet aus X_L', 199),
    ('L - Induktivitaet aus Fluss', 200),
    ('L - Induktivitaet aus Thomsonformel', 201),
    ('L - Induktivitaet aus Eigenkreisfrequenz', 202),
    ('N - Windungszahl aus Spulenfeld', 203),
    ('N - Windungszahl aus Feldstaerke', 204),
    ('N - Windungszahl aus Drahtdurchmesser', 205),
    ('N - Windungszahl aus Flussverkettung', 206),
    ('N1 - Primaerwindungen aus Spannung', 207),
    ('N1 - Primaerwindungen aus Stromverhaeltnis', 208),
    ('N2 - Sekundaerwindungszahl', 209),
    ('N2 - Sekundaerwindungen aus Stromverhaeltnis', 210),
    ('P - elektrische Leistung', 211),
    ('P - Leistung am Widerstand', 212),
    ('P - Wirkleistung Wechselstrom', 213),
    ('P - Wirkleistung aus Scheinleistung', 214),
    ('P_V - Verlustleistung in Leitung', 215),
    ('P_V - Verlustleistung aus Spannung', 216),
    ('P_V - Verlustleistung als Differenz', 217),
    ('Phi - magnetischer Fluss', 218),
    ('Phi - magnetischer Fluss aus Induktivitaet', 219),
    ('Phi - magnetischer Fluss aus B und Flaeche', 220),
    ('Phi_E - elektrischer Fluss', 221),
    ('Phi_E - elektrischer Fluss aus Ladung', 222),
    ('Q - Kondensatorladung', 223),
    ('Q - Ladung aus Strom und Zeit', 224),
    ('Q - Ladung aus Feldfluss', 225),
    ('Q_blind - Blindleistung', 226),
    ('Q_blind - Blindleistung aus S und P', 227),
    ('Q_blind - Blindleistung aus Scheinleistung', 228),
    ('Q_blind - Blindleistung der Spule', 229),
    ('Q_blind - Blindleistungsbetrag des Kondensators', 230),
    ('R - Ohmscher Widerstand', 231),
    ('R - Wirkwiderstand aus Impedanz', 232),
    ('R - Widerstand aus Leistung', 233),
    ('R - Widerstand aus Leistung und Spannung', 234),
    ('R - Drahtwiderstand', 235),
    ('R - Wirkwiderstand aus Leistungsfaktor', 236),
    ('S - Scheinleistung', 237),
    ('S - Scheinleistung aus P und Q', 238),
    ('T - Periodendauer', 239),
    ('T - Thomsonsche Schwingungsdauer', 240),
    ('T - Periodendauer aus Kreisfrequenz', 241),
    ('T - Periodendauer Federpendel', 242),
    ('T - Periodendauer Fadenpendel', 243),
    ('U - Spannung am Widerstand', 244),
    ('U - Spannung im homogenen E-Feld', 245),
    ('U0 - Spannungsamplitude Kondensator', 246),
    ('U0 - Scheitelspannung aus Effektivwert', 247),
    ('U1 - Primaerspannung Transformator', 248),
    ('U1 - Primaerspannung aus Stromverhaeltnis', 249),
    ('U2 - Sekundaerspannung Transformator', 250),
    ('U2 - Sekundaerspannung aus Stromverhaeltnis', 251),
    ('U_eff - Effektivspannung', 252),
    ('U_eff - Effektivspannung aus Leistung', 253),
    ('U_eff - Effektivspannung aus Strom und Impedanz', 254),
    ('U_ind - Induktionsspannung nach Faraday', 255),
    ('U_ind - Induktion durch Feldaenderung', 256),
    ('U_ind - Induktion durch Flaechenaenderung', 257),
    ('U_ind - Bewegungsinduktion am Leiter', 258),
    ('U_ind - Rahmen tritt in Magnetfeld ein/aus', 259),
    ('U_ind - Generator mit sinusfoermigem Feld', 260),
    ('U_ind - Dreieckgenerator / Dreiecksignal', 261),
    ('U_ind - Selbstinduktionsspannung', 262),
    ('U_ind - Bewegungsinduktion mit Winkel', 263),
    ('U_ind - Dreiecksignal Induktion', 264),
    ('U_max - Scheitelspannung', 265),
    ('U_max - Generator Sinus-Spannung', 266),
    ('W - mechanische Arbeit', 267),
    ('W - Arbeit aus Energiedifferenz', 268),
    ('W_el - elektrische Arbeit/Energie', 269),
    ('W_el - elektrische Arbeit aus Leistung', 270),
    ('X_C - kapazitiver Blindwiderstand', 271),
    ('X_C - kapazitiver Widerstand aus Amplituden', 272),
    ('X_L - induktiver Blindwiderstand', 273),
    ('X_L - induktiver Widerstand aus Amplituden', 274),
    ('Z - Impedanz RLC-Reihenschaltung', 275),
    ('Z - Impedanz RL-Reihe', 276),
    ('Z - Impedanz RC-Reihe', 277),
    ('a - Abstand paralleler Leiter', 278),
    ('a - Beschleunigung nach Newton', 279),
    ('a - Beschleunigung aus Geschwindigkeit', 280),
    ('a_max - Maximalbeschleunigung der Schwingung', 281),
    ('a_r - Radialbeschleunigung', 282),
    ('a_r - Radialbeschleunigung aus T', 283),
    ('beta - Geschwindigkeit relativ zu c', 284),
    ('beta - beta aus gamma', 285),
    ('cos_phi - Leistungsfaktor', 286),
    ('cos_phi - Leistungsfaktor aus Leistung', 287),
    ('cos_phi - Leistungsfaktor aus P und S', 288),
    ('d - Durchmesser aus Flaeche', 289),
    ('d - Durchmesser aus Radius', 290),
    ('d - Plattenabstand aus E-Feld', 291),
    ('eps0 - elektrische Feldkonstante', 292),
    ('eps_r - relative Permittivitaet', 293),
    ('eps_r - relative Permittivitaet aus Feldstaerken', 294),
    ('eta - Wirkungsgrad', 295),
    ('eta - Trafo-Wirkungsgrad', 296),
    ('eta - Wirkungsgrad aus Verlustleistung', 297),
    ('f - Frequenz aus Periodendauer', 298),
    ('f - Frequenz aus Kreisfrequenz', 299),
    ('f - Frequenz aus induktivem Blindwiderstand', 300),
    ('f - Frequenz aus kapazitivem Blindwiderstand', 301),
    ('f - Frequenz aus Sinus-Induktion', 302),
    ('f - Frequenz aus Dreiecksignal', 303),
    ('f0 - Resonanzfrequenz / Eigenfrequenz', 304),
    ('f0 - Resonanzfrequenz aus Periodendauer', 305),
    ('g - Fallbeschleunigung aus Fadenpendel', 306),
    ('gamma - Lorentzfaktor', 307),
    ('gamma - gamma aus Zeitdilatation', 308),
    ('h - Fallhoehe aus Geschwindigkeit', 309),
    ('h - Hoehe aus Lageenergie', 310),
    ('h - Fallhoehe aus Zeit', 311),
    ('l - Laenge eines Leiters im Magnetfeld', 312),
    ('l - Laenge aus Kraft auf stromdurchflossenen Leiter', 313),
    ('l - Spulenlaenge aus magnetischer Feldstaerke', 314),
    ('l - Spulenlaenge aus magnetischer Flussdichte', 315),
    ('l - Spulenlaenge aus Induktivitaet', 316),
    ('l - Drahtlaenge aus Widerstandsgesetz', 317),
    ('l - Wellenlaenge aus Wellengeschwindigkeit', 318),
    ('l - magnetische Weglaenge im Ringkern', 319),
    ('l_Draht - Drahtlaenge aus Windungszahl und Umfang', 320),
    ('l_Draht - Drahtlaenge aus Widerstandsgesetz', 321),
    ('m - Masse im Massenspektrometer', 322),
    ('m - Masse aus Beschleunigung und Kreisbahn', 323),
    ('mu0 - magnetische Feldkonstante', 324),
    ('mu_r - relative Permeabilitaet aus B', 325),
    ('mu_r - relative Permeabilitaet aus Induktivitaet', 326),
    ('mu_r - relative Permeabilitaet', 327),
    ('omega - Kreisfrequenz', 328),
    ('omega - Kreisfrequenz aus Periodendauer', 329),
    ('omega - Eigenkreisfrequenz LC', 330),
    ('omega - omega aus XL', 331),
    ('omega - omega aus XC', 332),
    ('omega - Kreisfrequenz aus Maximalgeschwindigkeit', 333),
    ('omega - Kreisfrequenz aus Maximalbeschleunigung', 334),
    ('p - Impuls', 335),
    ('p - Impulsaenderung', 336),
    ('q_m - spezifische Ladung q/m', 337),
    ('q_m - spezifische Ladung aus Kreisbahn', 338),
    ('r - Radius der Kreisbahn im B-Feld', 339),
    ('r - Radius aus Flaeche', 340),
    ('r - mittlerer Radius Ringkern', 341),
    ('rho - spezifischer Widerstand', 342),
    ('rho - spezifischer Widerstand aus U,I', 343),
    ('sin_phi - Blindleistungsfaktor aus Q und S', 344),
    ('tau - Zeitkonstante RL-Kreis', 345),
    ('tau - Zeitkonstante RC-Kreis', 346),
    ('v - Teilchengeschwindigkeit aus Kreisbahn', 347),
    ('v - Geschwindigkeit nach Beschleunigungsspannung', 348),
    ('v - Geschwindigkeit aus Fallhoehe', 349),
    ('v - Geschwindigkeit aus Bewegungsinduktion', 350),
    ('v_max - Maximalgeschwindigkeit der Schwingung', 351),
    ('v_filter - Geschwindigkeit im Wien-Filter', 352),
    ('v_filter - Filtergeschwindigkeit mit Plattenfeld', 353),
    ('l - Laenge eines Leiters im Magnetfeld', 312),
    ('DeltaPhi - Aenderung des magnetischen Flusses', 139),
    ('DeltaPhi - Flussaenderung aus Induktionsspannung', 140),
    ('U_ind - Induktionsspannung nach Faraday', 255),
    ('U_ind - Induktion durch Feldaenderung', 256),
    ('U_ind - Induktion durch Flaechenaenderung', 257),
    ('U_ind - Bewegungsinduktion am Leiter', 258),
    ('U_ind - Generator mit sinusfoermigem Feld', 260),
    ('U_ind - Dreieckgenerator / Dreiecksignal', 261),
    ('B - magnetische Flussdichte aus Fluss', 122),
    ('P - Leistung am Widerstand', 212),
    ('rho - spezifischer Widerstand', 342),
    ('E0 - Ruheenergie', 146),
    ('A - Kreisflaeche aus Durchmesser', 116),
    ('A - Rechteckflaeche', 117),
    ('Phi - magnetischer Fluss aus B und Flaeche', 220),
    ('U_ind - Bewegungsinduktion mit Winkel', 263),
    ('v - Geschwindigkeit aus Bewegungsinduktion', 350),
    ('B - B aus Bewegungsinduktion', 126),
    ('DeltaB - B-Aenderung aus Induktion', 135),
    ('DeltaA - Flaechenaenderung aus Induktion', 133),
    ('U_max - Generator Sinus-Spannung', 266),
    ('B_max - B-Amplitude aus Generator', 127),
    ('f - Frequenz aus Sinus-Induktion', 302),
    ('U_ind - Dreiecksignal Induktion', 264),
    ('f - Frequenz aus Dreiecksignal', 303),
    ('B_max - B-Amplitude aus Dreiecksignal', 128),
    ('Q - Ladung aus Feldfluss', 225),
    ('Phi_E - elektrischer Fluss aus Ladung', 222),
    ('DeltaA - Flaechenaenderung', 134),
    ('DeltaB - Magnetfeldaenderung', 136),
    ('I - Strom aus magnetischer Flussdichte einer Spule', 176),
    ('I - Strom aus magnetischer Feldstaerke', 177),
    ('I - Strom aus magnetischem Fluss und Induktivitaet', 178),
    ('N - Windungszahl aus Spulenfeld', 203),
    ('N - Windungszahl aus Feldstaerke', 204),
    ('mu_r - relative Permeabilitaet aus B', 325),
    ('mu_r - relative Permeabilitaet aus Induktivitaet', 326),
    ('A - Flaeche aus Induktivitaet', 114),
    ('B - B aus Feldstaerke und Permeabilitaet', 121),
    ('H - Feldstaerke aus B', 173),
    ('l - Spulenlaenge aus magnetischer Feldstaerke', 314),
    ('l - Spulenlaenge aus magnetischer Flussdichte', 315),
    ('l - Spulenlaenge aus Induktivitaet', 316),
    ('l - Drahtlaenge aus Widerstandsgesetz', 317),
    ('Phi - magnetischer Fluss', 218),
    ('Phi - magnetischer Fluss aus Induktivitaet', 219),
    ('B - Magnetfeld einer langen Spule', 123),
    ('H - magnetische Feldstaerke einer Spule', 174),
    ('mu0 - magnetische Feldkonstante', 324),
    ('mu_r - relative Permeabilitaet', 327),
    ('L - Induktivitaet aus Spulengeometrie', 197),
    ('L - Induktivitaet aus Selbstinduktion', 198),
    ('U_ind - Selbstinduktionsspannung', 262),
    ('DeltaI - Stromaenderung bei Selbstinduktion', 137),
    ('E_mag - Energie im Magnetfeld der Spule', 155),
    ('I - Strom aus magnetischer Energie', 183),
    ('tau - Zeitkonstante RL-Kreis', 345),
    ('v - Geschwindigkeit aus Fallhoehe', 349),
    ('A - Kreisflaeche aus Radius', 115),
    ('A - Drahtquerschnitt aus Widerstand', 118),
    ('d - Durchmesser aus Flaeche', 289),
    ('l - magnetische Weglaenge im Ringkern', 319),
    ('r - mittlerer Radius Ringkern', 341),
    ('l_Draht - Drahtlaenge aus Windungszahl und Umfang', 320),
    ('N - Windungszahl aus Drahtdurchmesser', 205),
    ('H - Feldstaerke Ringkern', 175),
    ('I - Strom im Ringkern aus Feldstaerke', 185),
    ('L - Induktivitaet aus Fluss', 200),
    ('N - Windungszahl aus Flussverkettung', 206),
    ('R - Drahtwiderstand', 235),
    ('rho - spezifischer Widerstand aus U,I', 343),
    ('E_mag - Energie im Magnetfeld ueber B,H,V', 156),
    ('E_mag - Energie ueber Leistung-Zeit-Flaeche', 157),
    ('DeltaI - Stromaenderung', 138),
    ('d - Durchmesser aus Radius', 290),
    ('l_Draht - Drahtlaenge aus Widerstandsgesetz', 321),
    ('Phi_E - elektrischer Fluss', 221),
    ('X_C - kapazitiver Blindwiderstand', 271),
    ('C - Kapazitaet aus X_C', 129),
    ('E - elektrische Feldstaerke aus Kraft', 144),
    ('E - homogenes elektrisches Feld', 145),
    ('U - Spannung im homogenen E-Feld', 245),
    ('F_el - elektrische Kraft', 169),
    ('F_el - Coulomb-Kraft', 170),
    ('W_el - elektrische Arbeit/Energie', 269),
    ('C - Kapazitaet Plattenkondensator', 132),
    ('Q - Kondensatorladung', 223),
    ('E_cap - Energie im Kondensator', 148),
    ('eps0 - elektrische Feldkonstante', 292),
    ('eps_r - relative Permittivitaet', 293),
    ('I0 - Stromamplitude am Kondensator', 186),
    ('U0 - Spannungsamplitude Kondensator', 246),
    ('I0 - Stromamplitude aus XC', 188),
    ('Q_blind - Blindleistung', 226),
    ('E_cap - Kondensatorenergie aus Q und U', 149),
    ('E_cap - Kondensatorenergie aus Ladung', 150),
    ('eps_r - relative Permittivitaet aus Feldstaerken', 294),
    ('tau - Zeitkonstante RC-Kreis', 346),
    ('I - Strom aus elektrischer Leistung', 180),
    ('I - Strom aus Wechselstromkreis', 182),
    ('l - Wellenlaenge aus Wellengeschwindigkeit', 318),
    ('R - Ohmscher Widerstand', 231),
    ('U - Spannung am Widerstand', 244),
    ('P - elektrische Leistung', 211),
    ('f - Frequenz aus Periodendauer', 298),
    ('T - Periodendauer', 239),
    ('omega - Kreisfrequenz', 328),
    ('U_eff - Effektivspannung', 252),
    ('U_max - Scheitelspannung', 265),
    ('I_eff - Effektivstrom', 194),
    ('X_L - induktiver Blindwiderstand', 273),
    ('L - Induktivitaet aus X_L', 199),
    ('Z - Impedanz RLC-Reihenschaltung', 275),
    ('DeltaPhi_phase - Phasenverschiebung im RLC-Kreis', 141),
    ('f0 - Resonanzfrequenz / Eigenfrequenz', 304),
    ('T - Thomsonsche Schwingungsdauer', 240),
    ('X_C - kapazitiver Widerstand aus Amplituden', 272),
    ('X_L - induktiver Widerstand aus Amplituden', 274),
    ('I0 - Stromamplitude aus XL', 187),
    ('omega - Kreisfrequenz aus Periodendauer', 329),
    ('omega - Eigenkreisfrequenz LC', 330),
    ('omega - omega aus XL', 331),
    ('omega - omega aus XC', 332),
    ('Z - Impedanz RL-Reihe', 276),
    ('Z - Impedanz RC-Reihe', 277),
    ('R - Wirkwiderstand aus Impedanz', 232),
    ('DeltaPhi_phase - Phasenwinkel aus Zeigerdiagramm', 142),
    ('DeltaPhi_phase - Phasenwinkel aus Leistungsfaktor', 143),
    ('cos_phi - Leistungsfaktor', 286),
    ('P - Wirkleistung Wechselstrom', 213),
    ('S - Scheinleistung', 237),
    ('I_eff - Effektivstrom aus Scheitelwert', 195),
    ('U_eff - Effektivspannung aus Leistung', 253),
    ('I_eff - Effektivstrom aus Wirkleistung', 196),
    ('f0 - Resonanzfrequenz aus Periodendauer', 305),
    ('P_V - Verlustleistung aus Spannung', 216),
    ('R - Widerstand aus Leistung', 233),
    ('R - Widerstand aus Leistung und Spannung', 234),
    ('Q_blind - Blindleistung aus S und P', 227),
    ('S - Scheinleistung aus P und Q', 238),
    ('U0 - Scheitelspannung aus Effektivwert', 247),
    ('cos_phi - Leistungsfaktor aus Leistung', 287),
    ('X_C - kapazitiver Blindwiderstand', 271),
    ('C - Kapazitaet aus X_C', 129),
    ('f - Frequenz aus induktivem Blindwiderstand', 300),
    ('f - Frequenz aus kapazitivem Blindwiderstand', 301),
    ('U_eff - Effektivspannung aus Strom und Impedanz', 254),
    ('R - Wirkwiderstand aus Leistungsfaktor', 236),
    ('Q_blind - Blindleistung', 226),
    ('P - Wirkleistung aus Scheinleistung', 214),
    ('Q_blind - Blindleistung aus Scheinleistung', 228),
    ('cos_phi - Leistungsfaktor aus P und S', 288),
    ('sin_phi - Blindleistungsfaktor aus Q und S', 344),
    ('Q_blind - Blindleistung der Spule', 229),
    ('Q_blind - Blindleistungsbetrag des Kondensators', 230),
    ('omega - Eigenkreisfrequenz LC', 354),
    ('f0 - Resonanzfrequenz LC', 355),
    ('T - Thomsonsche Schwingungsdauer', 356),
    ('L - Induktivitaet aus Thomsonformel', 357),
    ('C - Kapazitaet aus Thomsonformel', 358),
    ('q - Ladung im LC-Kreis', 359),
    ('I - Strom im LC-Kreis', 360),
    ('I0 - Maximalstrom aus Ladungsamplitude', 361),
    ('U - Kondensatorspannung', 362),
    ('Q - Ladung aus Kondensatorspannung', 363),
    ('E_cap - Energie im Kondensator', 364),
    ('E_mag - Energie in der Spule', 365),
    ('E - Gesamtenergie LC-Kreis', 366),
    ('I0 - Maximalstrom aus Anfangsspannung', 367),
    ('U0 - Spannungsmaximum aus Maximalstrom', 368),
    ('R - Verlustleistung im RLC-Kreis', 369),
    ('Q_guete - Guete Serien-RLC', 370),
    ('Delta f - Bandbreite aus Guete', 371),
    ('L - Induktivitaet aus Eigenkreisfrequenz', 202),
    ('C - Kapazitaet aus Eigenkreisfrequenz', 131),
    ('I1 - Primaerstrom am Transformator', 189),
    ('I2 - Sekundaerstrom am Transformator', 191),
    ('U2 - Sekundaerspannung Transformator', 250),
    ('U1 - Primaerspannung Transformator', 248),
    ('N2 - Sekundaerwindungszahl', 209),
    ('I2 - Sekundaerstrom idealer Transformator', 192),
    ('eta - Wirkungsgrad', 295),
    ('P_V - Verlustleistung in Leitung', 215),
    ('U2 - Sekundaerspannung aus Stromverhaeltnis', 251),
    ('U1 - Primaerspannung aus Stromverhaeltnis', 249),
    ('N1 - Primaerwindungen aus Spannung', 207),
    ('eta - Trafo-Wirkungsgrad', 296),
    ('eta - Wirkungsgrad aus Verlustleistung', 297),
    ('P_V - Verlustleistung als Differenz', 217),
    ('N1 - Primaerwindungen aus Stromverhaeltnis', 208),
    ('N2 - Sekundaerwindungen aus Stromverhaeltnis', 210),
    ('B - B aus Lorentzkraft auf Ladung', 124),
    ('F_L - Lorentzkraft auf Ladung', 165),
    ('v - Teilchengeschwindigkeit aus Kreisbahn', 347),
    ('q_m - spezifische Ladung q/m', 337),
    ('q_m - spezifische Ladung aus Kreisbahn', 338),
    ('v_filter - Geschwindigkeit im Wien-Filter', 352),
    ('E_kin - kinetische Energie aus Beschleunigungsspannung', 152),
    ('Q - Ladung aus Strom und Zeit', 224),
    ('W_el - elektrische Arbeit aus Leistung', 270),
    ('d - Plattenabstand aus E-Feld', 291),
    ('v_filter - Filtergeschwindigkeit mit Plattenfeld', 353),
    ('I - Strom aus Kraft auf Leiter im Magnetfeld', 179),
    ('l - Laenge aus Kraft auf stromdurchflossenen Leiter', 313),
    ('U_ind - Rahmen tritt in Magnetfeld ein/aus', 259),
    ('B - B aus Kraft auf stromdurchflossenen Leiter', 125),
    ('F_L - Kraft auf stromdurchflossenen Leiter', 166),
    ('r - Radius der Kreisbahn im B-Feld', 339),
    ('v - Geschwindigkeit nach Beschleunigungsspannung', 348),
    ('m - Masse im Massenspektrometer', 322),
    ('m - Masse aus Beschleunigung und Kreisbahn', 323),
    ('E_kin - kinetische Energie klassisch', 151),
    ('gamma - Lorentzfaktor', 307),
    ('E_kin - kinetische Energie relativistisch', 153),
    ('r - Radius aus Flaeche', 340),
    ('F - Kraft auf Leiter im Magnetfeld', 161),
    ('F - Kraft zwischen parallelen Leitern', 162),
    ('I1 - Strom paralleler Leiter', 190),
    ('I2 - Strom paralleler Leiter', 193),
    ('a - Abstand paralleler Leiter', 278),
    ('beta - beta aus gamma', 285),
    ('T - Periodendauer aus Frequenz', 372),
    ('f - Frequenz aus Periodendauer', 373),
    ('omega - Kreisfrequenz', 374),
    ('x - Auslenkung harmonische Schwingung', 375),
    ('v - Momentangeschwindigkeit', 376),
    ('v - Maximalgeschwindigkeit', 377),
    ('a - Beschleunigung harmonisch', 378),
    ('a - Maximalbeschleunigung', 379),
    ('F - Rueckstellkraft Feder', 380),
    ('T - Periodendauer Federpendel', 381),
    ('D - Federkonstante aus Periodendauer', 382),
    ('m - Masse aus Federpendel', 383),
    ('T - Periodendauer Fadenpendel', 384),
    ('l - Pendellaenge aus Periodendauer', 385),
    ('g - Fallbeschleunigung aus Pendel', 386),
    ('E - Gesamtenergie Federpendel', 387),
    ('E_sp - Spannenergie bei Auslenkung', 388),
    ('E_kin - Bewegungsenergie in Schwingung', 389),
    ('A_s - Amplitude aus Gesamtenergie', 390),
    ('phi - Phase', 391),
    ('f - Frequenz aus Kreisfrequenz', 299),
    ('T - Periodendauer aus Kreisfrequenz', 241),
    ('A_s - Amplitude aus Maximalgeschwindigkeit', 119),
    ('A_s - Amplitude aus Maximalbeschleunigung', 120),
    ('omega - Kreisfrequenz aus Maximalgeschwindigkeit', 333),
    ('omega - Kreisfrequenz aus Maximalbeschleunigung', 334),
    ('h - Fallhoehe aus Geschwindigkeit', 309),
    ('E_kin - kinetische Energie Mechanik', 154),
    ('E_pot - potentielle Energie', 158),
    ('W - mechanische Arbeit', 267),
    ('F - Newtonsche Kraft', 160),
    ('F_G - Gewichtskraft', 163),
    ('F_R - Reibungskraft', 167),
    ('p - Impuls', 335),
    ('a_r - Radialbeschleunigung', 282),
    ('F_r - Radialkraft', 171),
    ('E_pot - potentielle Energie aus Energieerhaltung', 159),
    ('W - Arbeit aus Energiedifferenz', 268),
    ('p - Impulsaenderung', 336),
    ('a_r - Radialbeschleunigung aus T', 283),
    ('F_r - Radialkraft aus Winkelgeschwindigkeit', 172),
    ('F_G - Gravitationskraft allgemein', 164),
    ('F_R - Reibungskraft aus Arbeit', 168),
    ('a - Beschleunigung nach Newton', 279),
    ('a - Beschleunigung aus Geschwindigkeit', 280),
    ('h - Hoehe aus Lageenergie', 310),
    ('h - Fallhoehe aus Zeit', 311),
    ('beta - Geschwindigkeit relativ zu c', 284),
    ('gamma - gamma aus Zeitdilatation', 308),
    ('E0 - Ruheenergie in eV', 147),
    ('I - Strom aus Leistung am Widerstand', 181),
    ('I - Stromstaerke nach Ohm', 184),
]

CHAPTERS = [
    (0, 568),
    (568, 1077),
    (1645, 992),
    (2637, 759),
    (3396, 651),
    (4047, 751),
    (4798, 609),
    (5407, 893),
    (6300, 785),
    (7085, 741),
    (7826, 771),
    (8597, 686),
    (9283, 626),
    (9909, 669),
    (10578, 372),
    (10950, 577),
    (11527, 597),
    (12124, 520),
    (12644, 663),
    (13307, 455),
    (13762, 477),
    (14239, 640),
    (14879, 603),
    (15482, 677),
    (16159, 608),
    (16767, 649),
    (17416, 671),
    (18087, 766),
    (18853, 495),
    (19348, 503),
    (19851, 705),
    (20556, 561),
    (21117, 593),
    (21710, 647),
    (22357, 561),
    (22918, 557),
    (23475, 675),
    (24150, 623),
    (24773, 748),
    (25521, 908),
    (26429, 426),
    (26855, 423),
    (27278, 319),
    (27597, 391),
    (27988, 341),
    (28329, 311),
    (28640, 301),
    (28941, 410),
    (29351, 269),
    (29620, 342),
    (29962, 383),
    (30345, 334),
    (30679, 340),
    (31019, 324),
    (31343, 308),
    (31651, 312),
    (31963, 334),
    (32297, 297),
    (32594, 324),
    (32918, 310),
    (33228, 320),
    (33548, 363),
    (33911, 307),
    (34218, 252),
    (34470, 307),
    (34777, 277),
    (35054, 273),
    (35327, 274),
    (35601, 335),
    (35936, 341),
    (36277, 266),
    (36543, 316),
    (36859, 224),
    (37083, 202),
    (37285, 215),
    (37500, 234),
    (37734, 236),
    (37970, 207),
    (38177, 227),
    (38404, 218),
    (38622, 317),
    (38939, 328),
    (39267, 297),
    (39564, 358),
    (39922, 332),
    (40254, 255),
    (40509, 232),
    (40741, 232),
    (40973, 261),
    (41234, 237),
    (41471, 273),
    (41744, 282),
    (42026, 282),
    (42308, 269),
    (42577, 324),
    (42901, 347),
    (43248, 268),
    (43516, 293),
    (43809, 354),
    (44163, 293),
    (44456, 307),
    (44763, 285),
    (45048, 313),
    (45361, 285),
    (45646, 299),
    (45945, 285),
    (46230, 321),
    (46551, 311),
    (46862, 314),
    (47176, 345),
    (47521, 325),
    (47846, 246),
    (48092, 255),
    (48347, 225),
    (48572, 334),
    (48906, 239),
    (49145, 255),
    (49400, 251),
    (49651, 272),
    (49923, 278),
    (50201, 283),
    (50484, 276),
    (50760, 295),
    (51055, 324),
    (51379, 290),
    (51669, 302),
    (51971, 267),
    (52238, 283),
    (52521, 267),
    (52788, 255),
    (53043, 262),
    (53305, 292),
    (53597, 274),
    (53871, 294),
    (54165, 229),
    (54394, 266),
    (54660, 234),
    (54894, 331),
    (55225, 213),
    (55438, 306),
    (55744, 361),
    (56105, 345),
    (56450, 304),
    (56754, 278),
    (57032, 269),
    (57301, 250),
    (57551, 184),
    (57735, 222),
    (57957, 274),
    (58231, 264),
    (58495, 245),
    (58740, 314),
    (59054, 291),
    (59345, 335),
    (59680, 218),
    (59898, 292),
    (60190, 276),
    (60466, 297),
    (60763, 236),
    (60999, 272),
    (61271, 191),
    (61462, 286),
    (61748, 318),
    (62066, 195),
    (62261, 272),
    (62533, 264),
    (62797, 262),
    (63059, 198),
    (63257, 243),
    (63500, 255),
    (63755, 255),
    (64010, 266),
    (64276, 245),
    (64521, 228),
    (64749, 283),
    (65032, 246),
    (65278, 392),
    (65670, 284),
    (65954, 326),
    (66280, 347),
    (66627, 263),
    (66890, 264),
    (67154, 302),
    (67456, 281),
    (67737, 211),
    (67948, 266),
    (68214, 273),
    (68487, 241),
    (68728, 242),
    (68970, 266),
    (69236, 279),
    (69515, 296),
    (69811, 271),
    (70082, 282),
    (70364, 261),
    (70625, 252),
    (70877, 261),
    (71138, 275),
    (71413, 317),
    (71730, 246),
    (71976, 233),
    (72209, 265),
    (72474, 292),
    (72766, 305),
    (73071, 254),
    (73325, 292),
    (73617, 240),
    (73857, 241),
    (74098, 242),
    (74340, 270),
    (74610, 284),
    (74894, 248),
    (75142, 303),
    (75445, 256),
    (75701, 282),
    (75983, 313),
    (76296, 249),
    (76545, 246),
    (76791, 342),
    (77133, 302),
    (77435, 271),
    (77706, 357),
    (78063, 257),
    (78320, 224),
    (78544, 225),
    (78769, 250),
    (79019, 274),
    (79293, 268),
    (79561, 324),
    (79885, 284),
    (80169, 324),
    (80493, 255),
    (80748, 269),
    (81017, 238),
    (81255, 234),
    (81489, 204),
    (81693, 264),
    (81957, 242),
    (82199, 262),
    (82461, 210),
    (82671, 262),
    (82933, 247),
    (83180, 257),
    (83437, 262),
    (83699, 213),
    (83912, 243),
    (84155, 255),
    (84410, 257),
    (84667, 245),
    (84912, 239),
    (85151, 273),
    (85424, 243),
    (85667, 256),
    (85923, 244),
    (86167, 287),
    (86454, 296),
    (86750, 341),
    (87091, 339),
    (87430, 300),
    (87730, 336),
    (88066, 373),
    (88439, 365),
    (88804, 288),
    (89092, 316),
    (89408, 337),
    (89745, 261),
    (90006, 301),
    (90307, 232),
    (90539, 221),
    (90760, 318),
    (91078, 236),
    (91314, 282),
    (91596, 271),
    (91867, 265),
    (92132, 251),
    (92383, 287),
    (92670, 237),
    (92907, 230),
    (93137, 273),
    (93410, 233),
    (93643, 233),
    (93876, 311),
    (94187, 276),
    (94463, 232),
    (94695, 261),
    (94956, 217),
    (95173, 241),
    (95414, 290),
    (95704, 254),
    (95958, 244),
    (96202, 195),
    (96397, 236),
    (96633, 229),
    (96862, 247),
    (97109, 277),
    (97386, 256),
    (97642, 246),
    (97888, 256),
    (98144, 214),
    (98358, 249),
    (98607, 253),
    (98860, 271),
    (99131, 298),
    (99429, 266),
    (99695, 317),
    (100012, 247),
    (100259, 267),
    (100526, 250),
    (100776, 230),
    (101006, 202),
    (101208, 240),
    (101448, 203),
    (101651, 397),
    (102048, 404),
    (102452, 329),
    (102781, 386),
    (103167, 359),
    (103526, 367),
    (103893, 310),
    (104203, 243),
    (104446, 309),
    (104755, 268),
    (105023, 312),
    (105335, 307),
    (105642, 298),
    (105940, 329),
    (106269, 331),
    (106600, 322),
    (106922, 248),
    (107170, 228),
    (107398, 250),
    (107648, 217),
    (107865, 227),
    (108092, 282),
    (108374, 302),
    (108676, 190),
    (108866, 209),
    (109075, 288),
    (109363, 280),
    (109643, 326),
    (109969, 236),
    (110205, 260),
    (110465, 326),
    (110791, 265),
    (111056, 288),
    (111344, 296),
    (111640, 254),
    (111894, 302),
    (112196, 361),
    (112557, 276),
    (112833, 265),
    (113098, 314),
    (113412, 330),
    (113742, 272),
    (114014, 260),
    (114274, 283),
    (114557, 253),
    (114810, 260),
    (115070, 257),
    (115327, 292),
    (115619, 300),
    (115919, 268),
    (116187, 243),
    (116430, 241),
    (116671, 281),
    (116952, 248),
    (117200, 273),
    (117473, 277),
    (117750, 270),
    (118020, 274),
    (118294, 273),
    (118567, 281),
    (118848, 260),
    (119108, 261),
    (119369, 259),
    (119628, 342),
    (119970, 300),
    (120270, 276),
    (120546, 274),
    (120820, 266),
    (121086, 256),
    (121342, 265),
    (121607, 268),
    (121875, 251),
    (122126, 292),
    (122418, 267),
    (122685, 272),
    (122957, 288),
    (123245, 275),
    (123520, 285),
    (123805, 260),
    (124065, 272),
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
PI = 3.141592653589793

CALC_CATS = (
    ("Grundgroessen", 0, 5),
    ("Mechanik Basis", 5, 8),
    ("Mechanische Schwingungen", 13, 15),
    ("Elektrische Schwingungen", 28, 11),
    ("Wechselstrom / RLC", 39, 24),
    ("Elektrisches Feld / Strom", 63, 9),
    ("Wellen", 72, 5),
    ("Magnetfeld / Induktion", 77, 5),
)

CALCS = (
    ("T aus f", "T = 1/f", "T", "s", (("f", "Hz"),), "T_FROM_F"),
    ("f aus T", "f = 1/T", "f", "Hz", (("T", "s"),), "F_FROM_T"),
    ("omega aus f", "omega = 2*pi*f", "omega", "rad/s", (("f", "Hz"),), "OMEGA_FROM_F"),
    ("f aus omega", "f = omega/(2*pi)", "f", "Hz", (("omega", "rad/s"),), "F_FROM_OMEGA"),
    ("T aus omega", "T = 2*pi/omega", "T", "s", (("omega", "rad/s"),), "T_FROM_OMEGA"),
    ("v aus s,t", "v = s/t", "v", "m/s", (("s", "m"), ("t", "s")), "V_FROM_S_T"),
    ("s aus v,t", "s = v*t", "s", "m", (("v", "m/s"), ("t", "s")), "S_FROM_V_T"),
    ("a aus dv,dt", "a = dv/dt", "a", "m/s^2", (("dv", "m/s"), ("dt", "s")), "A_FROM_DV_DT"),
    ("F aus m,a", "F = m*a", "F", "N", (("m", "kg"), ("a", "m/s^2")), "F_FROM_M_A"),
    ("Impuls", "p = m*v", "p", "kg*m/s", (("m", "kg"), ("v", "m/s")), "P_FROM_M_V"),
    ("E_kin", "E_kin = 0.5*m*v^2", "E_kin", "J", (("m", "kg"), ("v", "m/s")), "E_KIN"),
    ("E_pot", "E_pot = m*g*h", "E_pot", "J", (("m", "kg"), ("g", "m/s^2"), ("h", "m")), "E_POT"),
    ("Leistung", "P = W/t", "P", "W", (("W", "J"), ("t", "s")), "P_MECH"),
    ("T Federpendel", "T = 2*pi*sqrt(m/D)", "T", "s", (("m", "kg"), ("D", "N/m")), "T_SPRING"),
    ("D Federpendel", "D = 4*pi^2*m/T^2", "D", "N/m", (("m", "kg"), ("T", "s")), "D_SPRING"),
    ("m Federpendel", "m = D*T^2/(4*pi^2)", "m", "kg", (("D", "N/m"), ("T", "s")), "M_SPRING"),
    ("omega Feder", "omega = sqrt(D/m)", "omega", "rad/s", (("D", "N/m"), ("m", "kg")), "OMEGA_SPRING"),
    ("f Feder", "f = 1/(2*pi)*sqrt(D/m)", "f", "Hz", (("D", "N/m"), ("m", "kg")), "F_SPRING_OSC"),
    ("T Fadenpendel", "T = 2*pi*sqrt(l/g)", "T", "s", (("l", "m"), ("g", "m/s^2")), "T_PENDULUM"),
    ("l Fadenpendel", "l = g*T^2/(4*pi^2)", "l", "m", (("g", "m/s^2"), ("T", "s")), "L_PENDULUM"),
    ("v_max", "v_max = omega*A_s", "v_max", "m/s", (("omega", "rad/s"), ("A_s", "m")), "V_MAX"),
    ("a_max", "a_max = omega^2*A_s", "a_max", "m/s^2", (("omega", "rad/s"), ("A_s", "m")), "A_MAX"),
    ("E Federpendel", "E_ges = 0.5*D*A_s^2", "E_ges", "J", (("D", "N/m"), ("A_s", "m")), "E_SPRING"),
    ("A_s aus v_max", "A_s = v_max/omega", "A_s", "m", (("v_max", "m/s"), ("omega", "rad/s")), "A_FROM_VMAX_OMEGA"),
    ("A_s aus a_max", "A_s = a_max/omega^2", "A_s", "m", (("a_max", "m/s^2"), ("omega", "rad/s")), "A_FROM_AMAX_OMEGA"),
    ("omega aus v_max", "omega = v_max/A_s", "omega", "rad/s", (("v_max", "m/s"), ("A_s", "m")), "OMEGA_FROM_VMAX_A"),
    ("omega aus a_max", "omega = sqrt(a_max/A_s)", "omega", "rad/s", (("a_max", "m/s^2"), ("A_s", "m")), "OMEGA_FROM_AMAX_A"),
    ("g Fadenpendel", "g = 4*pi^2*l/T^2", "g", "m/s^2", (("l", "m"), ("T", "s")), "G_PENDULUM"),
    ("omega0 LC", "omega0 = 1/sqrt(L*C)", "omega0", "rad/s", (("L", "H"), ("C", "F")), "OMEGA_LC"),
    ("f0 LC", "f0 = 1/(2*pi*sqrt(L*C))", "f0", "Hz", (("L", "H"), ("C", "F")), "F_LC"),
    ("T LC", "T = 2*pi*sqrt(L*C)", "T", "s", (("L", "H"), ("C", "F")), "T_LC"),
    ("L aus T,C", "L = T^2/(4*pi^2*C)", "L", "H", (("T", "s"), ("C", "F")), "L_FROM_TC"),
    ("C aus T,L", "C = T^2/(4*pi^2*L)", "C", "F", (("T", "s"), ("L", "H")), "C_FROM_TL"),
    ("I0 aus U0", "I0 = U0*sqrt(C/L)", "I0", "A", (("U0", "V"), ("C", "F"), ("L", "H")), "I0_FROM_U0"),
    ("U0 aus I0", "U0 = I0*sqrt(L/C)", "U0", "V", (("I0", "A"), ("L", "H"), ("C", "F")), "U0_FROM_I0"),
    ("E Kondensator", "E = 0.5*C*U0^2", "E", "J", (("C", "F"), ("U0", "V")), "E_CAP_OSC"),
    ("E Spule", "E = 0.5*L*I0^2", "E", "J", (("L", "H"), ("I0", "A")), "E_COIL_OSC"),
    ("L aus omega0,C", "L = 1/(omega0^2*C)", "L", "H", (("omega0", "rad/s"), ("C", "F")), "L_FROM_OMEGA_C"),
    ("C aus omega0,L", "C = 1/(omega0^2*L)", "C", "F", (("omega0", "rad/s"), ("L", "H")), "C_FROM_OMEGA_L"),
    ("X_L", "X_L = 2*pi*f*L", "X_L", "Ohm", (("f", "Hz"), ("L", "H")), "XL"),
    ("X_C", "X_C = 1/(2*pi*f*C)", "X_C", "Ohm", (("f", "Hz"), ("C", "F")), "XC"),
    ("Z RLC Reihe", "Z = sqrt(R^2+(X_L-X_C)^2)", "Z", "Ohm", (("R", "Ohm"), ("X_L", "Ohm"), ("X_C", "Ohm")), "Z_RLC"),
    ("I_eff aus Z", "I_eff = U_eff/Z", "I_eff", "A", (("U_eff", "V"), ("Z", "Ohm")), "I_EFF"),
    ("P WSK", "P = U_eff*I_eff*cos_phi", "P", "W", (("U_eff", "V"), ("I_eff", "A"), ("cos_phi", "1")), "P_AC"),
    ("cos_phi", "cos_phi = R/Z", "cos_phi", "1", (("R", "Ohm"), ("Z", "Ohm")), "COS_PHI"),
    ("U_R", "U_R = I_eff*R", "U_R", "V", (("I_eff", "A"), ("R", "Ohm")), "U_R_AC"),
    ("U_L", "U_L = I_eff*X_L", "U_L", "V", (("I_eff", "A"), ("X_L", "Ohm")), "U_L_AC"),
    ("U_C", "U_C = I_eff*X_C", "U_C", "V", (("I_eff", "A"), ("X_C", "Ohm")), "U_C_AC"),
    ("L aus X_L,f", "L = X_L/(2*pi*f)", "L", "H", (("X_L", "Ohm"), ("f", "Hz")), "L_FROM_XL_F"),
    ("f aus X_L,L", "f = X_L/(2*pi*L)", "f", "Hz", (("X_L", "Ohm"), ("L", "H")), "F_FROM_XL_L"),
    ("C aus X_C,f", "C = 1/(2*pi*f*X_C)", "C", "F", (("X_C", "Ohm"), ("f", "Hz")), "C_FROM_XC_F"),
    ("f aus X_C,C", "f = 1/(2*pi*C*X_C)", "f", "Hz", (("X_C", "Ohm"), ("C", "F")), "F_FROM_XC_C"),
    ("U_eff aus I,Z", "U_eff = I_eff*Z", "U_eff", "V", (("I_eff", "A"), ("Z", "Ohm")), "U_EFF_FROM_IZ"),
    ("R aus Z,cos_phi", "R = Z*cos_phi", "R", "Ohm", (("Z", "Ohm"), ("cos_phi", "1")), "R_FROM_Z_COS"),
    ("Scheinleistung", "S = U_eff*I_eff", "S", "VA", (("U_eff", "V"), ("I_eff", "A")), "S_AC"),
    ("Blindleistung", "Q = U_eff*I_eff*sin_phi", "Q", "var", (("U_eff", "V"), ("I_eff", "A"), ("sin_phi", "1")), "Q_AC"),
    ("P aus S,cos_phi", "P = S*cos_phi", "P", "W", (("S", "VA"), ("cos_phi", "1")), "P_FROM_S_COS"),
    ("Q aus S,sin_phi", "Q = S*sin_phi", "Q", "var", (("S", "VA"), ("sin_phi", "1")), "Q_FROM_S_SIN"),
    ("S aus P,Q", "S = sqrt(P^2+Q^2)", "S", "VA", (("P", "W"), ("Q", "var")), "S_FROM_P_Q"),
    ("cos_phi aus P,S", "cos_phi = P/S", "cos_phi", "1", (("P", "W"), ("S", "VA")), "COS_FROM_P_S"),
    ("sin_phi aus Q,S", "sin_phi = Q/S", "sin_phi", "1", (("Q", "var"), ("S", "VA")), "SIN_FROM_Q_S"),
    ("Blindleistung Spule", "Q_L = I_eff^2*X_L", "Q_L", "var", (("I_eff", "A"), ("X_L", "Ohm")), "Q_L"),
    ("Blindleistung Kondensator", "Q_C = I_eff^2*X_C", "Q_C", "var", (("I_eff", "A"), ("X_C", "Ohm")), "Q_C"),
    ("U aus R,I", "U = R*I", "U", "V", (("R", "Ohm"), ("I", "A")), "U_OHM"),
    ("I aus U,R", "I = U/R", "I", "A", (("U", "V"), ("R", "Ohm")), "I_OHM"),
    ("R aus U,I", "R = U/I", "R", "Ohm", (("U", "V"), ("I", "A")), "R_OHM"),
    ("P aus U,I", "P = U*I", "P", "W", (("U", "V"), ("I", "A")), "P_UI"),
    ("Q aus C,U", "Q = C*U", "Q", "C", (("C", "F"), ("U", "V")), "Q_CU"),
    ("C aus Q,U", "C = Q/U", "C", "F", (("Q", "C"), ("U", "V")), "C_QU"),
    ("E Feld", "E = U/d", "E", "V/m", (("U", "V"), ("d", "m")), "E_FIELD"),
    ("F im E-Feld", "F = q*E", "F", "N", (("q", "C"), ("E", "N/C")), "F_QE"),
    ("Arbeit qU", "W = q*U", "W", "J", (("q", "C"), ("U", "V")), "W_QU"),
    ("c Welle", "c = lambda*f", "c", "m/s", (("lambda", "m"), ("f", "Hz")), "C_WAVE"),
    ("f Welle", "f = c/lambda", "f", "Hz", (("c", "m/s"), ("lambda", "m")), "F_WAVE"),
    ("lambda Welle", "lambda = c/f", "lambda", "m", (("c", "m/s"), ("f", "Hz")), "LAMBDA_WAVE"),
    ("T Welle", "T = lambda/c", "T", "s", (("lambda", "m"), ("c", "m/s")), "T_WAVE"),
    ("Wellenzahl", "k = 2*pi/lambda", "k", "1/m", (("lambda", "m"),), "K_WAVE"),
    ("Lorentzkraft", "F = q*v*B", "F", "N", (("q", "C"), ("v", "m/s"), ("B", "T")), "F_LORENTZ"),
    ("Leiterkraft", "F = B*I*l", "F", "N", (("B", "T"), ("I", "A"), ("l", "m")), "F_WIRE"),
    ("Induktion blv", "U_ind = B*l*v", "U_ind", "V", (("B", "T"), ("l", "m"), ("v", "m/s")), "U_IND_BLV"),
    ("Induktion N dPhi", "U_ind = N*dPhi/dt", "U_ind", "V", (("N", "1"), ("dPhi", "Wb"), ("dt", "s")), "U_IND_NPHI"),
    ("B aus Leiterkraft", "B = F/(I*l)", "B", "T", (("F", "N"), ("I", "A"), ("l", "m")), "B_WIRE"),
)

NUM_KEYS = (
    ("7", "8", "9", "DEL"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "E"),
    ("0", ".", "OK", ""),
)

KEYPAD_X = 7
KEYPAD_Y = 250
KEY_W = 72
KEY_H = 52
KEY_GAP = 6


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
                print("[DEBUG] Wissen gefunden. Das verdammte Pfadchaos hat verloren:", path)
            return handle
        except OSError:
            pass
    raise OSError("wissen.txt fehlt neben physchem_final.py")


def load_chapter(chapter_id):
    start, length = CHAPTERS[chapter_id]
    if DEBUG:
        print("[DEBUG] Kapitel laden. Bitte jetzt keinen Mist bauen:", chapter_id)
    handle = open_knowledge()
    try:
        remaining = start
        blocks_since_gc = 0
        # Kein seek(): PythonExtra stellt sich bei grossen Offsets gern bloed an.
        while remaining > 0:
            block_size = min(SKIP_BLOCK, remaining)
            skipped = handle.read(block_size)
            if len(skipped) != block_size:
                raise OSError("Byteposition ausserhalb von wissen.txt")
            remaining -= block_size
            del skipped
            blocks_since_gc += 1
            if blocks_since_gc == 16:
                # Der winzige Heap ist eine Diva, also regelmaessig aufraeumen.
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
    # Bytes sofort loswerden. Der kleine Speicher hat schon genug Stress.
    del data
    return text


def wrap_text(text, width):
    lines = []
    for raw in text.split("\n"):
        if raw == "":
            lines.append("")
            continue
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

    # Nach dem Lesen fliegt der Kram raus, sonst wird der RAM zur Muellhalde.
    del lines
    del text
    gc.collect()
    if DEBUG:
        print("[DEBUG] Artikel geschlossen. Der Heap darf wieder durchatmen.")
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


def show_text(title, text):
    lines = wrap_text(text, 39)
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
                elif event.key in (KEY_DEL, KEY_EXIT, KEY_EXE):
                    running = False
            elif event.type == KEYEV_TOUCH_UP:
                if event.y < HEADER_H and event.x < 70:
                    running = False
        time.sleep(0.01)
    del lines


def format_number(value):
    if value > -0.0000000001 and value < 0.0000000001:
        return "0"
    return "%.6g" % value


def need_nonzero(value, name):
    if value == 0:
        raise ValueError(name + " darf nicht 0 sein")
    return value


def need_sqrt(value):
    if value < 0:
        raise ValueError("Wurzel aus negativer Zahl")
    return value ** 0.5


def calc_value(calc_id, values):
    if calc_id == "T_FROM_F":
        return 1 / need_nonzero(values[0], "f")
    elif calc_id == "F_FROM_T":
        return 1 / need_nonzero(values[0], "T")
    elif calc_id == "OMEGA_FROM_F":
        return 2 * PI * values[0]
    elif calc_id == "F_FROM_OMEGA":
        return values[0] / (2 * PI)
    elif calc_id == "T_FROM_OMEGA":
        return 2 * PI / need_nonzero(values[0], "omega")
    elif calc_id == "V_FROM_S_T":
        return values[0] / need_nonzero(values[1], "t")
    elif calc_id == "S_FROM_V_T":
        return values[0] * values[1]
    elif calc_id == "A_FROM_DV_DT":
        return values[0] / need_nonzero(values[1], "dt")
    elif calc_id == "F_FROM_M_A":
        return values[0] * values[1]
    elif calc_id == "P_FROM_M_V":
        return values[0] * values[1]
    elif calc_id == "E_KIN":
        return 0.5 * values[0] * values[1] * values[1]
    elif calc_id == "E_POT":
        return values[0] * values[1] * values[2]
    elif calc_id == "P_MECH":
        return values[0] / need_nonzero(values[1], "t")
    elif calc_id == "T_SPRING":
        return 2 * PI * need_sqrt(values[0] / need_nonzero(values[1], "D"))
    elif calc_id == "D_SPRING":
        return 4 * PI * PI * values[0] / (need_nonzero(values[1], "T") ** 2)
    elif calc_id == "M_SPRING":
        return values[0] * values[1] * values[1] / (4 * PI * PI)
    elif calc_id == "OMEGA_SPRING":
        return need_sqrt(values[0] / need_nonzero(values[1], "m"))
    elif calc_id == "F_SPRING_OSC":
        return need_sqrt(values[0] / need_nonzero(values[1], "m")) / (2 * PI)
    elif calc_id == "T_PENDULUM":
        return 2 * PI * need_sqrt(values[0] / need_nonzero(values[1], "g"))
    elif calc_id == "L_PENDULUM":
        return values[0] * values[1] * values[1] / (4 * PI * PI)
    elif calc_id == "V_MAX":
        return values[0] * values[1]
    elif calc_id == "A_MAX":
        return values[0] * values[0] * values[1]
    elif calc_id == "E_SPRING":
        return 0.5 * values[0] * values[1] * values[1]
    elif calc_id == "A_FROM_VMAX_OMEGA":
        return values[0] / need_nonzero(values[1], "omega")
    elif calc_id == "A_FROM_AMAX_OMEGA":
        omega = need_nonzero(values[1], "omega")
        return values[0] / (omega * omega)
    elif calc_id == "OMEGA_FROM_VMAX_A":
        return values[0] / need_nonzero(values[1], "A_s")
    elif calc_id == "OMEGA_FROM_AMAX_A":
        return need_sqrt(values[0] / need_nonzero(values[1], "A_s"))
    elif calc_id == "G_PENDULUM":
        return 4 * PI * PI * values[0] / (need_nonzero(values[1], "T") ** 2)
    elif calc_id == "OMEGA_LC":
        return 1 / need_sqrt(need_nonzero(values[0] * values[1], "L*C"))
    elif calc_id == "F_LC":
        return 1 / (2 * PI * need_sqrt(need_nonzero(values[0] * values[1], "L*C")))
    elif calc_id == "T_LC":
        return 2 * PI * need_sqrt(values[0] * values[1])
    elif calc_id == "L_FROM_TC":
        return values[0] * values[0] / (4 * PI * PI * need_nonzero(values[1], "C"))
    elif calc_id == "C_FROM_TL":
        return values[0] * values[0] / (4 * PI * PI * need_nonzero(values[1], "L"))
    elif calc_id == "I0_FROM_U0":
        return values[0] * need_sqrt(values[1] / need_nonzero(values[2], "L"))
    elif calc_id == "U0_FROM_I0":
        return values[0] * need_sqrt(values[1] / need_nonzero(values[2], "C"))
    elif calc_id == "E_CAP_OSC":
        return 0.5 * values[0] * values[1] * values[1]
    elif calc_id == "E_COIL_OSC":
        return 0.5 * values[0] * values[1] * values[1]
    elif calc_id == "L_FROM_OMEGA_C":
        omega = need_nonzero(values[0], "omega0")
        return 1 / (omega * omega * need_nonzero(values[1], "C"))
    elif calc_id == "C_FROM_OMEGA_L":
        omega = need_nonzero(values[0], "omega0")
        return 1 / (omega * omega * need_nonzero(values[1], "L"))
    elif calc_id == "XL":
        return 2 * PI * values[0] * values[1]
    elif calc_id == "XC":
        return 1 / (2 * PI * need_nonzero(values[0], "f") * need_nonzero(values[1], "C"))
    elif calc_id == "Z_RLC":
        return need_sqrt(values[0] * values[0] + (values[1] - values[2]) * (values[1] - values[2]))
    elif calc_id == "I_EFF":
        return values[0] / need_nonzero(values[1], "Z")
    elif calc_id == "P_AC":
        return values[0] * values[1] * values[2]
    elif calc_id == "COS_PHI":
        return values[0] / need_nonzero(values[1], "Z")
    elif calc_id == "U_R_AC":
        return values[0] * values[1]
    elif calc_id == "U_L_AC":
        return values[0] * values[1]
    elif calc_id == "U_C_AC":
        return values[0] * values[1]
    elif calc_id == "L_FROM_XL_F":
        return values[0] / (2 * PI * need_nonzero(values[1], "f"))
    elif calc_id == "F_FROM_XL_L":
        return values[0] / (2 * PI * need_nonzero(values[1], "L"))
    elif calc_id == "C_FROM_XC_F":
        return 1 / (2 * PI * need_nonzero(values[0], "X_C") * need_nonzero(values[1], "f"))
    elif calc_id == "F_FROM_XC_C":
        return 1 / (2 * PI * need_nonzero(values[0], "X_C") * need_nonzero(values[1], "C"))
    elif calc_id == "U_EFF_FROM_IZ":
        return values[0] * values[1]
    elif calc_id == "R_FROM_Z_COS":
        return values[0] * values[1]
    elif calc_id == "S_AC":
        return values[0] * values[1]
    elif calc_id == "Q_AC":
        return values[0] * values[1] * values[2]
    elif calc_id == "P_FROM_S_COS":
        return values[0] * values[1]
    elif calc_id == "Q_FROM_S_SIN":
        return values[0] * values[1]
    elif calc_id == "S_FROM_P_Q":
        return need_sqrt(values[0] * values[0] + values[1] * values[1])
    elif calc_id == "COS_FROM_P_S":
        return values[0] / need_nonzero(values[1], "S")
    elif calc_id == "SIN_FROM_Q_S":
        return values[0] / need_nonzero(values[1], "S")
    elif calc_id == "Q_L":
        return values[0] * values[0] * values[1]
    elif calc_id == "Q_C":
        return values[0] * values[0] * values[1]
    elif calc_id == "U_OHM":
        return values[0] * values[1]
    elif calc_id == "I_OHM":
        return values[0] / need_nonzero(values[1], "R")
    elif calc_id == "R_OHM":
        return values[0] / need_nonzero(values[1], "I")
    elif calc_id == "P_UI":
        return values[0] * values[1]
    elif calc_id == "Q_CU":
        return values[0] * values[1]
    elif calc_id == "C_QU":
        return values[0] / need_nonzero(values[1], "U")
    elif calc_id == "E_FIELD":
        return values[0] / need_nonzero(values[1], "d")
    elif calc_id == "F_QE":
        return values[0] * values[1]
    elif calc_id == "W_QU":
        return values[0] * values[1]
    elif calc_id == "C_WAVE":
        return values[0] * values[1]
    elif calc_id == "F_WAVE":
        return values[0] / need_nonzero(values[1], "lambda")
    elif calc_id == "LAMBDA_WAVE":
        return values[0] / need_nonzero(values[1], "f")
    elif calc_id == "T_WAVE":
        return values[0] / need_nonzero(values[1], "c")
    elif calc_id == "K_WAVE":
        return 2 * PI / need_nonzero(values[0], "lambda")
    elif calc_id == "F_LORENTZ":
        return values[0] * values[1] * values[2]
    elif calc_id == "F_WIRE":
        return values[0] * values[1] * values[2]
    elif calc_id == "U_IND_BLV":
        return values[0] * values[1] * values[2]
    elif calc_id == "U_IND_NPHI":
        return values[0] * values[1] / need_nonzero(values[2], "dt")
    elif calc_id == "B_WIRE":
        return values[0] / need_nonzero(values[1] * values[2], "I*l")
    raise ValueError("Unbekannte Formel")


def key_label_at(x, y):
    if x < KEYPAD_X or y < KEYPAD_Y:
        return None, -1
    col = (x - KEYPAD_X) // (KEY_W + KEY_GAP)
    row = (y - KEYPAD_Y) // (KEY_H + KEY_GAP)
    if row < 0 or row >= 4 or col < 0 or col >= 4:
        return None, -1
    local_x = (x - KEYPAD_X) - col * (KEY_W + KEY_GAP)
    local_y = (y - KEYPAD_Y) - row * (KEY_H + KEY_GAP)
    if local_x >= KEY_W or local_y >= KEY_H:
        return None, -1
    return NUM_KEYS[row][col], row * 4 + col


def draw_number_input(name, unit, formula, text, message, selected_key):
    dclear(BG)
    draw_header("Eingabe " + name, True)
    dtext_opt(12, 55, DIM, C_NONE, DTEXT_LEFT, DTEXT_TOP, formula[:38], -1)
    dtext_opt(12, 82, FG, C_NONE, DTEXT_LEFT, DTEXT_TOP, name + " [" + unit + "]", -1)
    drect(12, 112, SCREEN_W - 12, 158, C_WHITE)
    shown = text
    if shown == "":
        shown = "_"
    if len(shown) > 22:
        shown = shown[-22:]
    dtext_opt(20, 135, FG, C_NONE, DTEXT_LEFT, DTEXT_MIDDLE, shown, -1)
    dtext_opt(12, 173, DIM, C_NONE, DTEXT_LEFT, DTEXT_TOP, message[:38], -1)
    row = 0
    while row < 4:
        col = 0
        while col < 4:
            label = NUM_KEYS[row][col]
            x = KEYPAD_X + col * (KEY_W + KEY_GAP)
            y = KEYPAD_Y + row * (KEY_H + KEY_GAP)
            color = SELECTED if row * 4 + col == selected_key else BG
            drect(x, y, x + KEY_W, y + KEY_H, color)
            dline(x, y, x + KEY_W, y, DIM)
            dline(x, y + KEY_H, x + KEY_W, y + KEY_H, DIM)
            dline(x, y, x, y + KEY_H, DIM)
            dline(x + KEY_W, y, x + KEY_W, y + KEY_H, DIM)
            if label != "":
                dtext_opt(x + KEY_W // 2, y + KEY_H // 2, FG, C_NONE, DTEXT_CENTER, DTEXT_MIDDLE, label, -1)
            col += 1
        row += 1


def append_number_char(text, key):
    if len(text) >= 24:
        return text
    if key >= "0" and key <= "9":
        return text + key
    if key == ".":
        part = text
        pos = text.find("E")
        if pos >= 0:
            part = text[pos + 1:]
        if part.find(".") < 0:
            return text + key
        return text
    if key == "-":
        if text == "" or text.endswith("E"):
            return text + key
        return text
    if key == "E":
        if text != "" and text != "-" and text.find("E") < 0:
            return text + key
        return text
    return text


def input_number(name, unit, formula):
    text = ""
    message = "SI-Einheit eingeben"
    selected_key = 0
    running = True
    while running:
        draw_number_input(name, unit, formula, text, message, selected_key)
        dupdate()
        cleareventflips()
        events = poll_events()
        for event in events:
            key = None
            if event.type == KEYEV_DOWN:
                if event.key == KEY_LEFT:
                    selected_key = max(0, selected_key - 1)
                elif event.key == KEY_RIGHT:
                    selected_key = min(15, selected_key + 1)
                elif event.key == KEY_UP:
                    selected_key = max(0, selected_key - 4)
                elif event.key == KEY_DOWN:
                    selected_key = min(15, selected_key + 4)
                elif event.key == KEY_DEL:
                    text = text[:-1]
                elif event.key == KEY_EXIT:
                    return None
                elif event.key == KEY_EXE:
                    key = NUM_KEYS[selected_key // 4][selected_key % 4]
            elif event.type == KEYEV_TOUCH_UP:
                if event.y < HEADER_H and event.x < 70:
                    return None
                key, touched = key_label_at(event.x, event.y)
                if touched >= 0:
                    selected_key = touched
            if key == "DEL":
                text = text[:-1]
            elif key == "OK":
                try:
                    return float(text)
                except ValueError:
                    message = "Ungueltige Zahl"
                except OverflowError:
                    message = "Zahl zu gross"
            elif key is not None and key != "":
                text = append_number_char(text, key)
        time.sleep(0.01)
    return None


def run_calc(calc):
    title, formula, result_name, result_unit, params, calc_id = calc
    values = []
    index = 0
    while index < len(params):
        name, unit = params[index]
        value = input_number(name, unit, formula)
        if value is None:
            return
        values.append(value)
        index += 1
    try:
        result = calc_value(calc_id, values)
        body = formula + "\n\n" + result_name + " = " + format_number(result) + " " + result_unit
    except ValueError as error:
        body = formula + "\n\nFehler:\n" + str(error)
    except OverflowError as error:
        body = formula + "\n\nFehler:\n" + str(error)
    del values
    gc.collect()
    show_text(title, body)


def open_calculator():
    category_index = select_list("Physik-Rechner", CALC_CATS, True)
    while category_index is not None:
        category_title, calc_start, calc_count = CALC_CATS[category_index]
        calcs = list_rows(CALCS, calc_start, calc_count)
        calc_index = select_list(category_title, calcs, True)
        while calc_index is not None:
            run_calc(calcs[calc_index])
            calc_index = select_list(category_title, calcs, True)
        del calcs
        gc.collect()
        category_index = select_list("Physik-Rechner", CALC_CATS, True)


def run():
    main_rows = []
    index = 0
    while index < len(MODES):
        main_rows.append(MODES[index])
        index += 1
    main_rows.append(("Physik-Rechner", 0, 0))
    main_rows.append(("Beenden", 0, 0))
    while True:
        mode_index = select_list("Physik LK On-Demand", main_rows, False)
        if mode_index is None:
            return
        if mode_index == len(MODES):
            open_calculator()
            continue
        if mode_index == len(MODES) + 1:
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
