#!/usr/bin/env python3
"""
File Search Assistant - v1.0
A privacy-first desktop application for intelligent file search and quick path autofill.
Instantly find and autofill file paths in any application using global hotkeys.
"""

import sys
import os
from pathlib import Path

# Add the app directory to Python path
app_dir = Path(__file__).parent / "app"
sys.path.insert(0, str(app_dir))

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from ui.main_window import MainWindow
from core.logging_config import setup_logging


def main():
    """Main application entry point."""
    # Setup logging
    setup_logging()
    
    # Create Qt application
    app = QApplication(sys.argv)
    app.setApplicationName("File Search Assistant")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("File Search Assistant")
    
    # Load stylesheet
    try:
        style_path = app_dir / "ui" / "styles.qss"
        if style_path.exists():
            with open(style_path, "r") as f:
                app.setStyleSheet(f.read())
            # Set a dark palette as fallback/base for standard widgets not covered by QSS
            from PySide6.QtGui import QPalette, QColor
            palette = QPalette()
            palette.setColor(QPalette.Window, QColor(18, 18, 18))
            palette.setColor(QPalette.WindowText, QColor(224, 224, 224))
            palette.setColor(QPalette.Base, QColor(30, 30, 30))
            palette.setColor(QPalette.AlternateBase, QColor(18, 18, 18))
            palette.setColor(QPalette.ToolTipBase, QColor(30, 30, 30))
            palette.setColor(QPalette.ToolTipText, QColor(224, 224, 224))
            palette.setColor(QPalette.Text, QColor(224, 224, 224))
            palette.setColor(QPalette.Button, QColor(30, 30, 30))
            palette.setColor(QPalette.ButtonText, QColor(224, 224, 224))
            palette.setColor(QPalette.BrightText, Qt.red)
            palette.setColor(QPalette.Link, QColor(0, 229, 255))
            palette.setColor(QPalette.Highlight, QColor(0, 229, 255))
            palette.setColor(QPalette.HighlightedText, Qt.black)
            app.setPalette(palette)
    except Exception as e:
        print(f"Failed to load stylesheet: {e}")
    
    # High DPI handling is enabled by default in Qt6; deprecated attributes removed
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Start event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


