# TIPE – Elliptic-Curve Cryptography Experiments

This repository contains a collection of educational experiments around elliptic-curve cryptography (ECC) and the ElGamal cryptosystem. The codebase includes reusable math/cryptography utilities, example scripts, and a report PDF.

## Setup

Create a virtual environment and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> **Note:** The scripts assume the repository root is on the Python path. Run them from the repository root using the `-m` flag.

## Running scripts

Examples:

```bash
python -m scripts.el_gamal_demo
python -m scripts.baby_step_giant_step_demo
python -m scripts.transfert_point_elgamal
python -m scripts.transfert_message_elgamal_demo
python -m scripts.elliptic_curve_basic_demo
```

## Project structure

```
.
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── data/
│   ├── features/
│   ├── models/
│   │   ├── baby_step_elliptic.py
│   │   ├── baby_step_elliptic_mod.py
│   │   ├── baby_step_giant_step.py
│   │   ├── el_gamal.py
│   │   ├── el_gamal_elliptic.py
│   │   ├── elliptic_curve.py
│   │   ├── elliptic_curve_basic.py
│   │   ├── elliptic_curve_mod.py
│   │   ├── point.py
│   │   └── transfert_message_elgamal.py
│   ├── utils/
│   │   ├── calcul_on_fq.py
│   │   ├── expo.py
│   │   └── operation_modulaire.py
│   └── visualization/
├── notebooks/
├── scripts/
│   ├── baby_step_giant_step_demo.py
│   ├── demonstration1.py
│   ├── el_gamal_demo.py
│   ├── elliptic_curve_basic_demo.py
│   ├── find_point.py
│   ├── generation_exemple1.py
│   ├── transfert_message_elgamal_demo.py
│   └── transfert_point_elgamal.py
├── reports/
│   ├── TIPE_ZAIDAN_Oscar.pdf
│   └── figures/
└── tests/
```

## Notes

- Reusable ECC/ElGamal logic lives in `src/models` and `src/utils`.
- Scripts in `scripts/` are small runnable demos or exploratory utilities.
- The PDF report has been moved to `reports/`.
