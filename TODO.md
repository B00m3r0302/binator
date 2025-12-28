# TODO — One-line Task List

## Milestone 1 — Setup & CLI
- Initialize git repo and virtualenv
- Create CLI entrypoint with scan/report commands
- Add logging and --help output

## Milestone 2 — Tool Wrappers
- Implement safe subprocess runner with timeout
- Wrap file command
- Wrap strings command
- Wrap readelf command
- Capture stdout/stderr and metadata

## Milestone 3 — ELF Parsing
- Integrate pyelftools
- Extract ELF headers and sections
- Extract interpreter and dynamic libs
- Compute file hashes and metadata
- Write normalized facts.json output

## Milestone 4 — Rule Engine
- Design findings schema and severity levels
- Implement NX check
- Implement PIE check
- Implement RELRO check
- Implement stack canary detection
- Implement stripped binary detection
- Implement suspicious string heuristics
- Compute overall score

## Milestone 5 — Reporting
- Implement rich terminal tables
- Implement summary output
- Implement Markdown report export
- Add recommended next-steps section

## Milestone 6 — Polish
- Add unit tests for parsers
- Add unit tests for rules
- Add demo binaries
- Write final README usage examples
