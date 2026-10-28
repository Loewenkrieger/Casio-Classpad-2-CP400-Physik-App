"""Physik-LK-App mit Wissen, das per Byteindex aus wissen.txt geladen wird."""

from gint import *
"""Small indexed records, loaded on demand without seek or eval."""


def store_text(block):
    return block if isinstance(block, str) else block.decode("ascii")


def skip_store(handle, remaining):
    if remaining < 0:
        raise ValueError("Ungueltige Datenposition")
    blocks = 0
    while remaining:
        chunk = handle.read(min(SKIP_BLOCK, remaining))
        if not chunk:
            raise ValueError("Datendatei ist verkuerzt")
        remaining -= len(chunk)
        del chunk
        blocks += 1
        if blocks % 16 == 0:
            gc.collect()


def open_store(kind):
    filename = "wissen.txt" if kind == 0 else "bilder.dat"
    for path in sibling_paths(filename):
        try:
            handle = open(path, "rb")
        except OSError:
            continue
        try:
            if store_text(handle.read(len(STORE_HEADERS[kind]))) != STORE_HEADERS[kind]:
                raise ValueError(filename + " passt nicht zu dieser App")
        except Exception:
            handle.close()
            raise
        return handle
    raise OSError(filename + " fehlt neben der App")


def record_value(text, position=0, depth=0):
    if depth > 6 or position >= len(text):
        raise ValueError("Ungueltiger Datensatz")
    tag = text[position]
    end = text.find(":", position + 1)
    if end < 0 or end - position > 12:
        raise ValueError("Ungueltiger Datensatzkopf")
    number = int(text[position + 1:end])
    position = end + 1
    if tag == "i":
        return number, position
    if tag == "s":
        if number < 0 or position + number > len(text):
            raise ValueError("Text im Datensatz verkuerzt")
        return text[position:position + number], position + number
    if tag != "t" or number < 0 or number > 32:
        raise ValueError("Unbekannter Datensatztyp")
    values = []
    for i in range(number):
        value, position = record_value(text, position, depth + 1)
        values.append(value)
    return tuple(values), position


def decode_record(block):
    text = store_text(block)
    value, end = record_value(text)
    if text[end:].strip():
        raise ValueError("Unerwartete Daten im Datensatz")
    return value


class DiskTable:
    def __init__(self, kind, count, start, width):
        self.kind = kind
        self.count = count
        self.start = start
        self.width = width

    def __len__(self):
        return self.count

    def open_rows(self, start):
        handle = open_store(self.kind)
        try:
            skip_store(handle, self.start + start * self.width - len(STORE_HEADERS[self.kind]))
        except Exception:
            handle.close()
            raise
        return handle

    def read_one(self, handle):
        block = handle.read(self.width)
        if len(block) != self.width:
            raise ValueError("Datensatz fehlt oder ist verkuerzt")
        return decode_record(block)

    def __getitem__(self, index):
        if index < 0:
            index += self.count
        if not 0 <= index < self.count:
            raise IndexError("Datensatz ausserhalb des Verzeichnisses")
        handle = self.open_rows(index)
        try:
            return self.read_one(handle)
        finally:
            handle.close()

    def __iter__(self):
        handle = self.open_rows(0)
        try:
            for i in range(self.count):
                yield self.read_one(handle)
        finally:
            handle.close()

    def read_rows(self, start, count):
        if start < 0 or count < 0 or start + count > self.count:
            raise IndexError("Menue ausserhalb des Verzeichnisses")
        rows = []
        handle = self.open_rows(start)
        try:
            for i in range(count):
                rows.append(self.read_one(handle))
        finally:
            handle.close()
        return rows


class DiskMap:
    def __init__(self, kind, count, start, width):
        self.table = DiskTable(kind, count, start, width)
        self.last_key = None
        self.last_value = None

    def __len__(self):
        return len(self.table)

    def get(self, key, default=None):
        if self.last_key is not None and key == self.last_key:
            return self.last_value
        handle = self.table.open_rows(0)
        try:
            for i in range(len(self.table)):
                name, value = self.table.read_one(handle)
                if name == key:
                    self.last_key, self.last_value = key, value
                    return value
        finally:
            handle.close()
        return default

    def __getitem__(self, key):
        value = self.get(key)
        if value is None:
            raise KeyError(key)
        return value

    def __contains__(self, key):
        return self.get(key) is not None

    def items(self):
        return iter(self.table)

    def __iter__(self):
        for key, value in self.table:
            yield key

    def values(self):
        for key, value in self.table:
            yield value


def load_chapter(chapter_id):
    start, length = CHAPTERS[chapter_id]
    handle = open_store(0)
    try:
        skip_store(handle, start - len(STORE_HEADERS[0]))
        data = handle.read(length)
    finally:
        handle.close()
    if len(data) != length:
        raise ValueError("Kapitel unvollstaendig")
    return store_text(data)

STORE_HEADERS = ('PCKNOW2 0483387abfbf9e15b57a728d\n', 'PCMEDIA2 7b728949c66e57f9a12819be\n')
MODES = DiskTable(0, 3, 33, 40)
CALC_CATS = DiskTable(0, 17, 153, 48)
CHAPTERS = DiskTable(0, 514, 969, 48)
SECTIONS = DiskTable(0, 171, 25641, 48)
CALCS = DiskTable(0, 167, 33849, 152)
CALC_NOTES = DiskMap(0, 81, 59233, 208)
ARTICLE_MEDIA = DiskMap(0, 32, 76081, 48)
ENTRIES = DiskTable(0, 840, 77617, 72)
MEDIA_HEADER = b'PCMEDIA2 7b728949c66e57f9a12819be\n'
MEDIA_INDEX = DiskMap(1, 39, 34, 224)
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

SKIP_BLOCK = 512
PI = 3.141592653589793



NUM_KEYS = (
    ("7", "8", "9", "DEL"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "E"),
    ("0", ".", "OK", "Einheit"),
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








def wrap_text(text, width):
    lines = []
    for raw in text.split("\n"):
        if raw == "":
            lines.append("")
            continue
        line = ""
        for word in raw.split(" "):
            while len(word) > width:
                if line:
                    lines.append(line)
                    line = ""
                lines.append(word[:width])
                word = word[width:]
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
    if hasattr(source, "read_rows"):
        return source.read_rows(start, count)
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
    if hasattr(rows, "read_rows"):
        rows = rows.read_rows(0, len(rows))
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
    try:
        text = load_chapter(chapter_id)
    except (OSError, ValueError, MemoryError) as error:
        show_text('Wissen nicht verfuegbar', str(error))
        return
    lines = wrap_text(text, 38)
    scroll = 0
    media = ARTICLE_MEDIA.get(chapter_id, ())
    bottom = SCREEN_H - 48 if media else SCREEN_H
    max_scroll = max(0, len(lines) * 18 - (bottom - HEADER_H - 12))
    running = True
    while running:
        dclear(BG)
        y = HEADER_H + 8 - scroll
        for line in lines:
            if y > HEADER_H - 18 and y < SCREEN_H:
                dtext_opt(8, y, FG, C_NONE, DTEXT_LEFT, DTEXT_TOP, line, -1)
            y += 18
        draw_header(title, True)
        if media:
            drect(0, bottom, SCREEN_W, SCREEN_H, SELECTED)
            dtext_opt(160, bottom + 24, FG, C_NONE, DTEXT_CENTER, DTEXT_MIDDLE, 'Abbildungen (EXE)', -1)
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
                elif event.key == KEY_EXE and media:
                    show_media(media)
                elif event.key in (KEY_DEL, KEY_EXIT):
                    running = False
            elif event.type == KEYEV_TOUCH_UP:
                if event.y < HEADER_H and event.x < 70:
                    running = False
                elif media and event.y >= bottom:
                    show_media(media)
                elif event.y >= HEADER_H:
                    scroll = max(0, scroll - 72) if event.y < (HEADER_H + bottom) // 2 else min(max_scroll, scroll + 72)
        time.sleep(0.01)
    del lines
    del text
    gc.collect()
    return




def show_text(title, text):
    lines = wrap_text(text, 38)
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
                elif event.y >= HEADER_H:
                    scroll = max(0,scroll-72) if event.y < (SCREEN_H+HEADER_H)//2 else min(max_scroll,scroll+72)
        time.sleep(0.01)
    del lines


def format_number(value):
    finite(value)
    if value == 0:
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
    if calc_id.startswith("Q_"):
        return finite(quantum_value(calc_id, values))
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
            return text
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


def input_number(name, unit, formula, default_unit=None):
    text = ""
    options = unit_options(unit)
    unit_index = 0
    for i in range(len(options)):
        if options[i][0] == default_unit:
            unit_index = i
    message = "Einheit wechselt die Eingabeeinheit"
    selected_key = 0
    running = True
    while running:
        draw_number_input(name, options[unit_index][0], formula, text, message, selected_key)
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
            elif key == "Einheit":
                unit_index = (unit_index + 1) % len(options)
                message = "Zahl gilt jetzt in " + options[unit_index][0]
            elif key == "OK":
                try:
                    return scaled_input(text, options, unit_index)
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
    if calc_id.startswith("FIT_"):
        run_fit(calc)
        return
    values = []
    index = 0
    while index < len(params):
        param = params[index]
        name, unit = param[0], param[1]
        value = input_number(name, unit, formula, param[2] if len(param) > 2 else None)
        if value is None:
            return
        values.append(value)
        index += 1
    try:
        result = calc_value(calc_id, values)
        body = formula + "\n\n" + result_text(result_name, result, result_unit)
        if calc_id in CALC_NOTES:
            body += "\n\nGeltung:\n" + CALC_NOTES[calc_id]
    except (ValueError, OverflowError, ZeroDivisionError) as error:
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
    main_rows.append(('Physik-Rechner', 0, 0))
    main_rows.append(('Beenden', 0, 0))
    while True:
        mode_index = select_list('Physik LK', main_rows, False)
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
                show_article(title, chapter_id)
                entry_index = select_list(section_title, entries, True)
            del entries
            gc.collect()
            section_index = select_list(mode_title, sections, True)
        del sections
        gc.collect()


"""Embedded by the builder; not a separate file on the calculator."""
import math

H_PLANCK = 6.62607015e-34
E_CHARGE = 1.602176634e-19
LIGHT_C = 299792458.0
M_E = 9.1093837139e-31
BOHR_A = 5.29177210544e-11
UNITS = {
    "m": (("m", 1), ("nm", 1e-9), ("pm", 1e-12), ("um", 1e-6), ("mm", 1e-3)),
    "J": (("J", 1), ("eV", E_CHARGE), ("keV", E_CHARGE * 1000)),
    "V": (("V", 1), ("kV", 1000)),
    "s": (("s", 1), ("ns", 1e-9), ("ps", 1e-12), ("fs", 1e-15)),
    "Hz": (("Hz", 1), ("THz", 1e12)),
}


def finite(value):
    if value != value or value == float("inf") or value == -float("inf"):
        raise ValueError("Zahl nicht endlich / zu gross")
    return value


def positive(value):
    finite(value)
    if value <= 0:
        raise ValueError("Wert muss groesser als 0 sein")
    return value


def natural(value):
    positive(value)
    if value != int(value):
        raise ValueError("Quantenzahl muss ganzzahlig sein")
    return value


def nonnegative(value):
    finite(value)
    if value < 0:
        raise ValueError("Wert darf nicht negativ sein")
    return value


def classical_v(value):
    if value >= LIGHT_C * 0.1:
        raise ValueError("v >= 0.1 c: relativistisch rechnen")
    return value


def box_energy(a, n, mass=M_E):
    # Factored to avoid squaring h before division on small-float runtimes.
    p = H_PLANCK * natural(n) / (2 * positive(a))
    return (p / positive(mass)) * p / 2


def quantum_value(ident, values):
    k = ident[2:]
    v = values
    if k not in ("LEVEL_D", "LEVEL_L", "LEVEL_F"):
        for value in v:
            nonnegative(value)
    if k == "EF": return H_PLANCK * positive(v[0])
    if k == "EL": return H_PLANCK * LIGHT_C / positive(v[0])
    if k == "FE": return positive(v[0]) / H_PLANCK
    if k == "LE": return H_PLANCK * LIGHT_C / positive(v[0])
    if k in ("PL", "LP", "DB", "PD"): return H_PLANCK / positive(v[0])
    if k == "PE": return positive(v[0]) / LIGHT_C
    if k == "EP": return positive(v[0]) * LIGHT_C
    if k == "NE": return v[0] / positive(v[1])
    if k == "EN": return v[0] * positive(v[1])
    if k == "NPT": return v[0] * v[1] / positive(v[2])
    if k == "PN": return v[0] * positive(v[1]) / positive(v[2])
    if k == "TN": return v[0] * positive(v[1]) / positive(v[2])
    if k in ("KF", "KL"):
        energy = H_PLANCK * positive(v[0]) if k == "KF" else H_PLANCK * LIGHT_C / positive(v[0])
        result = energy - v[1]
        if result < 0: raise ValueError("Kein Photoeffekt: unter Schwelle")
        return result
    if k in ("UK", "EXU"): return v[0] / E_CHARGE
    if k in ("KU", "EU", "EX"): return E_CHARGE * v[0]
    if k in ("WF", "WL"):
        result = H_PLANCK * v[0] - E_CHARGE * v[1] if k == "WF" else H_PLANCK * LIGHT_C / positive(v[0]) - v[1]
        if result < 0: raise ValueError("Negative Austrittsarbeit: Daten pruefen")
        return result
    if k == "FG": return v[0] / H_PLANCK
    if k == "WFG": return H_PLANCK * v[0]
    if k in ("LG", "WLG"): return H_PLANCK * LIGHT_C / positive(v[0])
    if k == "VK": return classical_v(math.sqrt(2 * v[0] / M_E))
    if k == "FKW": return (v[0] + v[1]) / H_PLANCK
    if k == "LKW": return H_PLANCK * LIGHT_C / positive(v[0] + v[1])
    if k == "LMV": return H_PLANCK / positive(v[0]) / positive(classical_v(v[1]))
    if k == "VD": return classical_v(H_PLANCK / positive(v[0]) / positive(v[1]))
    if k == "MD": return H_PLANCK / positive(classical_v(v[0])) / positive(v[1])
    if k == "LK":
        classical_v(math.sqrt(2 * positive(v[1]) / positive(v[0])))
        return H_PLANCK / math.sqrt(2 * v[0]) / math.sqrt(v[1])
    if k == "KD":
        p = H_PLANCK / positive(v[1])
        classical_v(p / positive(v[0]))
        return (p / v[0]) * p / 2
    if k in ("LUC", "LUR"):
        energy = E_CHARGE * positive(v[0])
        if k == "LUC": classical_v(math.sqrt(2 * energy / M_E))
        result = H_PLANCK / math.sqrt(2 * M_E) / math.sqrt(energy)
        if k == "LUR": result /= math.sqrt(1 + energy / (2 * M_E * LIGHT_C * LIGHT_C))
        return result
    if k == "UD":
        speed = classical_v(H_PLANCK / M_E / positive(v[0]))
        return (M_E / E_CHARGE) * speed * speed / 2
    if k in ("BL", "BD", "BT", "RL", "RR"):
        n = natural(v[-1])
        if k in ("BL", "BD"):
            if not 0 < v[1] <= 90: raise ValueError("Glanzwinkel: 0 < theta <= 90")
            sine = math.sin(v[1] * PI / 180)
            if k == "BL": return 2 * positive(v[0]) * sine / n
            return n * positive(v[0]) / (2 * sine)
        if k in ("BT", "RR"):
            ratio = n * positive(v[0]) / (2 * positive(v[1]))
            if ratio > 1: raise ValueError("Bragg-Bedingung nicht erfuellbar")
            angle = math.asin(ratio)
            if k == "BT": return angle * 180 / PI
            if angle >= PI / 4: raise ValueError("Ring trifft vorderen Schirm nicht")
            return positive(v[2]) * math.tan(2 * angle)
        return 2 * positive(v[0]) * math.sin(math.atan(positive(v[1]) / positive(v[2])) / 2) / n
    if k in ("DS", "DL", "DD", "DDIST"):
        for value in v: positive(value)
        return v[0] * v[1] / v[2]
    if k in ("SP", "SX"): return H_PLANCK / (4 * PI) / positive(v[0])
    if k in ("SV", "SXV"): return H_PLANCK / (4 * PI) / positive(v[0]) / positive(v[1])
    if k == "SVE": return H_PLANCK / (4 * PI * M_E) / positive(v[0])
    if k in ("SF", "ST"): return 1 / (4 * PI * positive(v[0]))
    if k in ("GF", "GT"): return (2 * math.log(2) / PI) / positive(v[0])
    if k in ("SCHOOL", "SCHOOLT"): return 1 / positive(v[0])
    if k in ("GAMMA", "TAU"): return H_PLANCK / (2 * PI) / positive(v[0])
    if k == "BOX_L": return 2 * positive(v[0]) / natural(v[1])
    if k == "BOX_P": return H_PLANCK * natural(v[1]) / (2 * positive(v[0]))
    if k == "BOX_E": return box_energy(v[0], v[1])
    if k == "BOX_EM": return box_energy(v[0], v[1], v[2])
    if k == "BOX_A": return H_PLANCK * natural(v[1]) / math.sqrt(8 * M_E) / math.sqrt(positive(v[0]))
    if k in ("BOX_D", "BOX_PH"):
        delta = abs(box_energy(v[0], v[1]) - box_energy(v[0], v[2]))
        positive(delta)
        return delta if k == "BOX_D" else H_PLANCK * LIGHT_C / delta
    if k in ("BOHR", "ION", "RAD", "H_D", "H_PH"):
        z = natural(v[0])
        n = natural(v[1])
        if k == "RAD": return BOHR_A * n * n / z
        energy = 13.6 * E_CHARGE * (z / n) ** 2
        if k == "BOHR": return -energy
        if k == "ION": return energy
        nf = natural(v[2])
        delta = abs(energy - 13.6 * E_CHARGE * (z / nf) ** 2)
        positive(delta)
        return delta if k == "H_D" else H_PLANCK * LIGHT_C / delta
    if k in ("LEVEL_D", "LEVEL_L", "LEVEL_F"):
        for value in v: finite(value)
        delta = positive(abs(v[0] - v[1]))
        if k == "LEVEL_D": return delta
        if k == "LEVEL_L": return H_PLANCK * LIGHT_C / delta
        return delta / H_PLANCK
    if k in ("EXL", "XR", "XU"): return (H_PLANCK * LIGHT_C / E_CHARGE) / positive(v[0])
    if k in ("COMP", "COMPL"):
        theta = v[-1]
        if theta > 180: raise ValueError("Streuwinkel: 0 bis 180 Grad")
        delta = H_PLANCK / M_E / LIGHT_C * (1 - math.cos(theta * PI / 180))
        return delta if k == "COMP" else positive(v[0]) + delta
    raise ValueError("Unbekannte Quantenformel")


def unit_options(unit):
    return UNITS.get(unit, ((unit, 1),))


def scaled_input(text, options, selected):
    value = finite(float(text))
    if value == 0:
        for char in text.upper().split("E")[0]:
            if "1" <= char <= "9":
                raise ValueError("Wert zu klein fuer diese Laufzeit")
    result = finite(value * options[selected][1])
    if value != 0 and result == 0:
        raise ValueError("Wert zu klein fuer diese Laufzeit")
    return result


def result_text(name, value, unit):
    finite(value)
    result = name + " = " + format_number(value) + " " + unit
    if unit == "J": result += "\n= " + format_number(value / E_CHARGE) + " eV"
    elif unit == "m" and value != 0 and abs(value) < 1e-6:
        scale, label = (1e-12, "pm") if abs(value) < 1e-9 else (1e-9, "nm")
        result += "\n= " + format_number(value / scale) + " " + label
    elif unit == "V" and abs(value) >= 1000:
        result += "\n= " + format_number(value / 1000) + " kV"
    return result


def fit_planck(points, wavelength=False):
    if not 2 <= len(points) <= 10: raise ValueError("2 bis 10 Messpunkte erforderlich")
    xs, ys = [], []
    for x, y in points:
        positive(x)
        nonnegative(y)
        xs.append((LIGHT_C / x if wavelength else x) / 1e14)
        ys.append(y / E_CHARGE if wavelength else y)
    xm, ym = sum(xs) / len(xs), sum(ys) / len(ys)
    spread = sum((x - xm) ** 2 for x in xs)
    if spread <= 0: raise ValueError("Frequenzen muessen verschieden sein")
    slope = sum((xs[i] - xm) * (ys[i] - ym) for i in range(len(xs))) / spread
    positive(slope)
    intercept = ym - slope * xm
    if intercept > 0: raise ValueError("Fit ergibt negative Austrittsarbeit")
    h_fit = finite(slope * E_CHARGE / 1e14)
    work = finite(-intercept * E_CHARGE)
    residual = sum((ys[i] - slope * xs[i] - intercept) ** 2 for i in range(len(xs)))
    return h_fit, work, finite(work / positive(h_fit)), math.sqrt(residual / len(xs))


def run_fit(calc):
    ident = calc[-1]
    wavelength = ident.startswith("FIT_L")
    count = 2
    if ident.endswith("N"):
        entered = input_number("Messpunkte (3-10)", "1", calc[1])
        if entered is None: return
        if entered != int(entered) or not 3 <= entered <= 10:
            show_text("Messreihe", "Bitte 3 bis 10 ganze Messpunkte.")
            return
        count = int(entered)
    points = []
    for i in range(count):
        label = "Punkt " + str(i + 1) + "/" + str(count)
        x = input_number("lambda" if wavelength else "f", "m" if wavelength else "Hz", label, "nm" if wavelength else "THz")
        if x is None: return
        y = input_number("E_kin" if wavelength else "U_G", "J" if wavelength else "V", label, "eV" if wavelength else "V")
        if y is None: return
        points.append((x, y))
    try:
        h_fit, work, threshold, rms = fit_planck(points, wavelength)
        body = result_text("h_fit", h_fit, "Js") + "\n\n" + result_text("W_A", work, "J")
        body += "\n\n" + result_text("f_G", threshold, "Hz")
        body += "\n\nRMS=" + format_number(rms) + (" eV" if wavelength else " V")
        body += "\nUngewichteter Fit; keine Fehlerabschaetzung. Konstanten bleiben unveraendert."
    except (ValueError, OverflowError, ZeroDivisionError) as error:
        body = "Fehler: " + str(error)
    show_text("Planck-Messreihe", body)

"""Embedded static-media viewer; no seek, image cache or PNG/JPEG decoder."""
MEDIA_STAGE = "Start"
MEDIA_RAM = -1


def media_stage(label):
    global MEDIA_STAGE, MEDIA_RAM
    MEDIA_STAGE = label
    MEDIA_RAM = memory_free()


def media_error(error, ident):
    after = memory_free()
    body = "Bild: " + ident + "\nFehler: " + type(error).__name__
    body += "\nSchritt: " + MEDIA_STAGE
    body += "\nRAM vor Schritt: " + str(MEDIA_RAM) + " B"
    body += "\nRAM nach Fehler: " + str(after) + " B"
    body += "\nDetails: " + (str(error) or "keine Zusatzmeldung")
    if MEDIA_RAM < 0 or after < 0: body += "\nRAM -1: nicht verfuegbar."
    return body + "\nTheorie und Rechner bleiben nutzbar."


def sibling_paths(filename):
    source = globals().get("__file__", "")
    slash = max(source.rfind("/"), source.rfind("\\"))
    paths = [source[:slash + 1] + filename] if slash >= 0 else []
    return paths + ["Python/" + filename, "/Python/" + filename, filename]


def fill_media(readinto, target):
    # Bypass text decoding, including ports that ignore the rb mode.
    view = memoryview(target)
    position = 0
    while position < len(view):
        part = view[position:min(position + SKIP_BLOCK, len(view))]
        count = readinto(part)
        if not isinstance(count, int) or count < 0 or count > len(part):
            raise ValueError("Ungueltige Byteanzahl beim Lesen")
        if count == 0: raise ValueError("bilder.dat ist verkuerzt")
        position += count


def read_media(ident):
    media_stage("Bildverzeichnis")
    row = MEDIA_INDEX[ident]
    start, length = row[2], row[3]
    handle = None
    media_stage("Datei oeffnen")
    for path in sibling_paths("bilder.dat"):
        try:
            handle = open(path, "rb")
            break
        except OSError:
            pass
    if handle is None: raise OSError("bilder.dat fehlt neben der App")
    try:
        media_stage("Paketkennung pruefen")
        readinto = getattr(handle, "readinto", None)
        if readinto is None: raise ValueError("PythonExtra ohne bytegenaues readinto")
        header = bytearray(len(MEDIA_HEADER))
        fill_media(readinto, header)
        if header != MEDIA_HEADER:
            raise ValueError("bilder.dat passt nicht zu dieser App")
        del header
        media_stage("Bildposition suchen")
        remaining = start - len(MEDIA_HEADER)
        if remaining < 0: raise ValueError("Ungueltige Bildposition")
        skip = memoryview(bytearray(SKIP_BLOCK))
        blocks = 0
        while remaining:
            size = min(SKIP_BLOCK, remaining)
            fill_media(readinto, skip[:size])
            remaining -= size
            blocks += 1
            if blocks % 16 == 0: gc.collect()
        del skip
        gc.collect()
        media_stage("Bildpuffer anlegen")
        buffer = bytearray(length)
        media_stage("Bilddaten lesen")
        fill_media(readinto, buffer)
        media_stage("Pruefsumme pruefen")
        if sum(buffer) % 65536 != row[6]: raise ValueError("Abbildung beschaedigt")
        return buffer
    finally:
        handle.close()


def rgb_word(word):
    return C_RGB((word >> 11) & 31, ((word >> 5) & 63) // 2, word & 31)


def draw_media(ident, data):
    row = MEDIA_INDEX[ident]
    kind, width, height = (row[1], row[4], row[5])
    if kind == 'V':
        media_stage('Vektorskizze zeichnen')
        for line in str(data, 'ascii').split('\n'):
            if not line:
                continue
            parts = line.split(' ', 4 if line.startswith('T ') else 5)
            if parts[0] == 'T':
                x, y, color = (int(parts[1]), int(parts[2]), int(parts[3]))
                dtext_opt(x + 8, y + 68, rgb_word(color), C_NONE, DTEXT_LEFT, DTEXT_TOP, parts[4], -1)
            elif parts[0] == 'L':
                dline(int(parts[1]) + 8, int(parts[2]) + 68, int(parts[3]) + 8, int(parts[4]) + 68, rgb_word(int(parts[5])))
            else:
                raise ValueError('Unbekannter Zeichenbefehl')
        return
    media_stage('Rasterdaten pruefen')
    if kind not in ('P4', 'P8'):
        raise ValueError('Unbekanntes Bildformat')
    count = 16 if kind == 'P4' else 256
    stride = (width + 1) // 2 if count == 16 else width
    expected = 2 * count + stride * height
    if len(data) != expected:
        raise ValueError('Ungueltige Pixeldaten')
    media_stage('Palette vorbereiten')
    view = memoryview(data)
    palette = view[:2 * count]
    pixels = view[2 * count:]
    constructor = globals().get('image_p4_rgb565' if count == 16 else 'image_p8_rgb565')
    if constructor is None:
        raise ValueError('PythonExtra ohne P4/P8-Bild-API')
    media_stage('Bildobjekt erzeugen')
    image_obj = constructor(width, height, pixels, palette)
    media_stage('Rasterbild zeichnen')
    draw_part = globals().get('dsubimage')
    if draw_part is None:
        raise ValueError('PythonExtra ohne Teilbild-API')
    for top in range(0, height, 128):
        draw_part(8, 68 + top, image_obj, 0, top, width, min(128, height - top))
    del image_obj, pixels, palette, view


def render_media_page(ident, position, total):
    media_stage('Bildansicht vorbereiten')
    dclear(C_WHITE)
    row = MEDIA_INDEX[ident]
    draw_header(row[0], True)
    dtext_opt(160, 47, FG, C_NONE, DTEXT_CENTER, DTEXT_TOP, str(position + 1) + ' / ' + str(total), -1)
    data = read_media(ident)
    draw_media(ident, data)
    del data
    gc.collect()
    media_stage('Bildbeschriftung')
    for i, line in enumerate(wrap_text(row[7], 38)[:4]):
        dtext_opt(8, 400 + i * 18, FG, C_NONE, DTEXT_LEFT, DTEXT_TOP, line, -1)
    drect(0, 482, 319, 527, SELECTED)
    for x, label in ((55, '<'), (162, '>'), (267, 'Zurueck')):
        dtext_opt(x, 505, FG, C_NONE, DTEXT_CENTER, DTEXT_MIDDLE, label, -1)
    media_stage('Bildschirm aktualisieren')
    dupdate()
    return


def show_media(ids):
    if not ids: return
    index = 0
    dirty = True
    while True:
        if dirty:
            try:
                media_stage("Bildansicht")
                render_media_page(ids[index],index,len(ids))
            except (OSError, ValueError, TypeError, AttributeError, MemoryError, KeyError, IndexError, OverflowError) as error:
                gc.collect()
                show_text("Abbildung nicht verfuegbar",media_error(error,ids[index]))
                return
            dirty = False
        cleareventflips()
        for event in poll_events():
            direction = 0
            if event.type == KEYEV_DOWN:
                if event.key in (KEY_DEL,KEY_EXIT,KEY_EXE): return
                if event.key == KEY_LEFT: direction = -1
                elif event.key == KEY_RIGHT: direction = 1
            elif event.type == KEYEV_TOUCH_UP:
                if event.y < HEADER_H and event.x < 70: return
                if event.y >= 482:
                    if event.x >= 215: return
                    direction = -1 if event.x < 110 else 1
            if direction:
                index = (index + direction) % len(ids)
                gc.collect()
                dirty = True
        time.sleep(0.01)





run()
