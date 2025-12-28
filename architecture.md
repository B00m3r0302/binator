# Project Steps & Architecture — Automated Binary Recon Pipeline

## High-level architecture
CLI -> Scanner -> Parsers -> Rule Engine -> Reporter

## Core components
- CLI entrypoint (scan, report)
- Scanner: safe subprocess wrappers
- Parsers: pyelftools + text parsers
- Rule engine: heuristic findings + score
- Reporter: terminal + markdown

## Output artifacts
- facts.json
- report.md

## Estimated total time
~21–30 hours
