# YOLO – Echtzeit-Objekterkennung

Ein Python-Projekt zur Erkennung von Objekten in einem Live-Kamerabild mit YOLO und OpenCV.

## Funktionen

- Zugriff auf eine Webcam.
- Echtzeit-Objekterkennung mit einem YOLO-Modell.
- Anzeige erkannter Objekte mit Begrenzungsrahmen und Klassenbezeichnungen.
- Anzeige der Anzahl erkannter Objekte und der Bildrate (FPS).
- Beenden mit `Q` oder `ESC`.
- Unit-Tests mit dem integrierten Python-Modul `unittest`.

## Voraussetzungen

- Python 3.10 oder neuer
- Eine Webcam
- Internetverbindung beim ersten Modellstart, sofern die Modelldatei noch nicht lokal vorhanden ist.

## Installation

Öffne das Terminal im Hauptverzeichnis des Projekts.

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Installiere die Abhängigkeiten:

```bash
python -m pip install -r requirements.txt
```

Installiere das Projekt im Entwicklungsmodus:

```bash
python -m pip install -e .
```

## Anwendung starten

```bash
python -m object_detection
```

Beim ersten Start lädt Ultralytics das Modell `yolo26n.pt`, falls es noch nicht lokal vorhanden ist.

- `Q`: Programm beenden
- `ESC`: Programm beenden

## Konfiguration

Die Einstellungen befinden sich in `src/object_detection/config.py`.

| Einstellung | Bedeutung | Standardwert |
|---|---|---|
| `MODEL_PATH` | YOLO-Modell | `yolo26n.pt` |
| `CAMERA_INDEX` | Kameraindex | `0` |
| `CONFIDENCE_THRESHOLD` | Mindest-Konfidenz | `0.40` |
| `IMAGE_SIZE` | Eingabegröße des Modells | `640` |
| `FRAME_WIDTH` | Kamerabreite | `1280` |
| `FRAME_HEIGHT` | Kamerahöhe | `720` |

Wenn die Webcam nicht geöffnet werden kann, kann ein anderer `CAMERA_INDEX` ausprobiert werden.

## Unit-Tests

Die Tests verwenden `unittest`. Eine zusätzliche Testbibliothek und eine Webcam sind dafür nicht erforderlich.

```bash
python -m unittest discover -s tests -v
```

Die Tests prüfen die FPS-Berechnung, die FPS-Glättung und die Erkennung der Beenden-Tasten.

## Projektstruktur

```text
YOLO_Object_Detection/
├── src/
│   └── object_detection/
│       ├── __init__.py
│       ├── __main__.py
│       ├── config.py
│       └── detector.py
├── tests/
│   ├── __init__.py
│   └── test_detector.py
├── .gitattributes
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Verwendete Technologien

- **Python** – Programmiersprache
- **Ultralytics YOLO** – Objekterkennung
- **OpenCV** – Kamera-Zugriff und Bildanzeige
- **unittest** – Unit-Tests

## Fehlerbehebung

| Problem | Mögliche Lösung |
|---|---|
| Kamera kann nicht geöffnet werden | Kamera-Verbindung prüfen und `CAMERA_INDEX` ändern |
| Modell kann nicht geladen werden | Internetverbindung und Modelldatei prüfen |
| Keine Objekte erkannt | Beleuchtung verbessern oder `CONFIDENCE_THRESHOLD` anpassen |
| Niedrige FPS | Kleinere Bildgröße oder leistungsfähigere Hardware verwenden |

## Hinweis

Das Programm benötigt eine funktionierende Kamera. Die Erkennungsqualität und Geschwindigkeit hängen vom Modell und der verfügbaren Hardware ab.

## Lizenz

MIT License
