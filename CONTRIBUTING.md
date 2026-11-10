# Contributing

Contributions can include device profiles, setup instructions, examples,
corrections and reports of successful or unsuccessful tests.

## Report a result or request support

Open an issue describing:

- The device and exact breakout-board model.
- The profile and its commit revision, if applicable.
- The Axiom model and firmware version.
- What you tried.
- What you expected and what actually happened.
- Relevant wiring details, readings, logs or photographs.

You can contribute useful feedback without editing a descriptor.

## Propose a change

1. Fork this repository if you do not have write access.
2. Create a branch for your change.
3. Make one focused improvement.
4. Open a pull request explaining the change and its evidence.

For a new integration, follow the profiles/AHT20 folder structure:

- profile.json: the importable device descriptor.
- metadata.json: source information and review status.
- README.md: requirements, setup, installation and expected behaviour.
- test-results/: reports for specific tested combinations.

Keep new integrations marked as draft until a maintainer reviews them.

## Document testing accurately

For hardware tests, copy the integration's test-report template to a
new dated file and complete it.

Record the exact profile commit, Axiom model, firmware, sensor board,
wiring and results. Link the completed report from metadata.json.

Preserve earlier reports so results remain traceable to the revisions
that were tested.

Documentation improvements do not require a hardware test. Explain
what you checked and identify any behaviour you could not verify.

## Preserve attribution

Identify the source of copied or adapted profiles, documentation and
examples. Preserve existing credits and record applicable licence
information.

## Review and publication

A maintainer reviews proposed changes and may request corrections or
additional evidence.

Acceptance of a change does not establish hardware compatibility.
Compatibility claims must refer to the combinations actually tested.

Adding a profile here does not automatically publish it in the
Device Library website or install it on an Axiom.