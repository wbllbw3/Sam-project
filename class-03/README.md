# Class 03 — Week 3 Progress

Check-in answers for this session, plus what the repository currently contains.

## 1) Project update

Sam's Project is a small full-stack web app — HTML/CSS, JavaScript/TypeScript, a Python data
service — and right now the repo, README, diagrams and license are in place while the app
itself is still a scaffold.

## 2) Scope for class 10

One working vertical slice: three pages, a typed TypeScript data module, a local JSON
endpoint, plus loading and error states, with auth, a database and frameworks explicitly
out of scope.

## 3) What I want done by week 3

- [ ] `index.html` + shared CSS rendering in the browser, navigation between pages working
- [ ] `tsconfig.json` in place; a typed `Task` module (`type Task`, `toggle()`) actually used by the page
- [ ] `/api/data` served by Python and rendered by the page, with a loading state and a visible error message
- [ ] Stretch: a short screen recording for the check-in

## 4) How

Build in the order data → types → UI: the Python endpoint returning fixed JSON first, then the
TypeScript module that types and fetches it, then the HTML/CSS wiring with explicit loading and
error branches. Dev loop is `tsc --watch` in one terminal and `python -m http.server` in the
other, so every change shows up on refresh. Each step is its own commit (endpoint, types, wiring),
which makes a regression obvious. Proof is a short clip of the happy path plus stopping the server
to show the error state, rather than claiming it works.

If time runs short, fall back to a static `data.json` and push the endpoint to next week — and say
so in advance instead of leaving it looking undone.

## What changed in the repo today

- Restructured the repository into a per-class submission layout (`class-01/` … `class-10/`)
- Root `README.md` is now the deliverables index
- Project background, stack and diagrams moved to [`docs/project-overview.md`](../docs/project-overview.md)
