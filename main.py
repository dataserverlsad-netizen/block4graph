from __future__ import annotations

import argparse
import os
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="TestRig Studio dashboard designer")
    parser.add_argument("--smoke", action="store_true", help="Run a headless smoke test and exit.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.smoke:
        os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

    from PyQt6.QtWidgets import QApplication
    from ui.main_window import MainWindow

    app = QApplication(sys.argv)
    window = MainWindow()
    if args.smoke:
        layout_path = window.run_smoke_test()
        print(f"Smoke test passed. Saved {layout_path}")
        window.close()
        return 0

    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())

