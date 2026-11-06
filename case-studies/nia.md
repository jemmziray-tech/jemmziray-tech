# NIA: building a private AI companion

NIA is my personal AI companion project. The source repository remains private; this case study describes its design without publishing credentials, conversations or deployment identifiers.

## Problem and current scope

The aim is to bring conversations, memory and planning into one personal workspace. The implemented milestone covers authenticated conversations and saved preferences. Memory, task tools, Calendar, action approvals and WhatsApp are future work.

The application uses Next.js and TypeScript for the interface, FastAPI for the backend, Firebase Authentication and Firestore for identity and storage, and Google ADK with a Gemini adapter for model interaction.

## Decisions and tradeoffs

| Decision | Reason | Tradeoff |
| --- | --- | --- |
| Verify identity on the server and restrict access to one owner | Keep private conversations within an explicit access boundary | This is not a multi-user product |
| Use transactional request IDs and generation leases | Handle retries without silently duplicating work | More state and failure handling to test |
| Prevent late responses from restoring deleted content | Make conversation deletion meaningful during in-flight generation | Requires coordination between storage and generation |
| Use emulators and a synthetic model for integration tests | Exercise UI and storage flows without paid calls or private data | These tests cannot establish live model quality |
| Keep unimplemented features labelled as future milestones | Avoid presenting a working-looking interface as completed integration | The first release has a deliberately narrow scope |

## Evidence and limitations

The repository includes backend, UI, API-client, emulator and browser integration tests, GitHub Actions checks, setup documentation and architecture decisions. The recent CI runs inspected during the November 2026 portfolio review passed.

Live Gemini is disabled by default. The repository documents that live provider availability and English/Swahili response quality have not yet been verified. No claims of autonomous planning, external messaging or real-world productivity gains are made here.

## Next evaluation

Before adding external actions, evaluate bilingual conversation quality with recorded scenarios, measure failure and retry behavior, and test owner-controlled memory deletion. Publish only aggregate results and synthetic examples; keep personal conversations private.
