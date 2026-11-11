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

The Catalogue connection reads profiles/<name>/metadata.json and profile.json from main.
Use a folder name of 1–80 letters, digits, dots, underscores or hyphens, beginning with a
letter or digit. Keep metadata.name and profile.deviceType equal to that folder name.
There is no separate index to maintain. Use the existing metadata schema; do not add a
targetPlatforms field. This is the Axiom library.

Once the coordinated service/web rollout is deployed, merging an approved PR makes the
profile available after the service refreshes. Open PRs stay in the Community feed.
The service never installs anything on Axiom: users explicitly add a profile to their draft,
review it, write the library and restart. A merge or an Installable label is not hardware
verification. Restricted profiles remain documented even when they cannot be added.

## Validate your changes

Run the repository checks with Python 3.13:

    python3 scripts/validate.py

These checks validate integration files and references. They do not
validate the complete firmware descriptor grammar or prove hardware
compatibility.

GitHub runs the same check on pull requests. Explain any remaining
testing limitations in your pull request.

## Contribution licensing

New contributions are submitted under the repository's ISC licence.
Contributors retain copyright in their contributions.

Only submit material you have the right to contribute under these terms.
Identify the source and licence of adapted material, and preserve
applicable copyright and licence notices.

## Maintainers and reviews

Initial maintainers:

- Nikos: @NikTheGeek1
- Sandy: @alexanderEnoch

Pull requests require one approving review from a code owner.
The pull request author cannot provide their own required approval.

Review considers correctness, documentation, attribution and the scope
of available test evidence. Approval does not establish compatibility
beyond the combinations actually tested.
