# Automated Binary Recon Pipeline (ctfrecon)

**One-line:** A terminal-first CLI tool that runs a battery of static checks on ELF binaries and produces a structured JSON facts file and a human-friendly Markdown report for CTF writeups and pentest recon.

## Features (MVP)
- Static analysis only (no execution)
- System tool wrappers: strings, file, readelf
- ELF parsing via pyelftools
- Rule engine (NX, PIE, RELRO, Canary, stripped, suspicious strings)
- JSON facts output
- Markdown report export
- Clean terminal output

## Usage (planned)
ctfrecon scan /path/to/binary -o facts.json
ctfrecon report facts.json --export report.md

## Why this project
High-ROI CTF/pentest tooling, pure terminal workflow, achievable in 20–40 hours, and highly demoable.

## License
MIT
