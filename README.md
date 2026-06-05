# TestRig Studio

TestRig Studio is a PyQt6 engineering dashboard designer for telemetry, test rigs, robotics, motors, batteries, sensors, and automation benches.

The application intentionally treats every data point as:

```text
topic value
```

Examples:

```text
rpm 5010
temperature 52.3
servo 90
```

## Run

```bash
pip install -r requirements.txt
python main.py
```

## Smoke Test

```bash
python main.py --smoke
```

## Features Included

- Free-form Qt Graphics View dashboard canvas
- Drag, resize, select, delete, copy, paste, snap-to-grid
- Collapsible draw bar with widget palette and live property editor
- Graph, numeric indicator, slider, button, input, switch, and gauge widgets
- Topic registry with auto-discovery
- `topic value` serial input parser
- Command bus output in `topic value` format
- JSON save/load for layouts
- SQLite session recording
- Replay of recorded sessions
- Built-in demo telemetry so the dashboard works without hardware

