# Phase Detector 🔍💧🔥

A simple Tkinter GUI tool to determine the phase of water based on temperature and pressure:
**Compressed liquid**, **Superheated vapor**, or **Two-phase mixture**.

## Features
- Simple Tkinter GUI
- Input by temperature or pressure
- Instant phase result
- Built-in saturation data (water)
- Great for thermodynamics learning

## Installation & Run
```bash
git clone https://github.com/username/phase-detector.git
cd phase-detector
pip install -r requirements.txt
python phase_detector.py
```

## Usage
1) Enter temperature (°C) or pressure (kPa)  
2) Choose comparison type (by temperature or pressure)  
3) Click **Check Phase**  
Examples:  
- 100 °C & 150 kPa → **Compressed liquid**  
- 100 °C & 101.3 kPa → **Two-phase mixture**

## Project Structure
```
phase-detector/
├─ phase_detector.py
├─ requirements.txt
├─ README.md
├─ LICENSE
├─ .gitignore
├─ docs/
└─ tests/
```

## Contributing
PRs are welcome. Fork → branch → commit → PR.

## License
MIT
