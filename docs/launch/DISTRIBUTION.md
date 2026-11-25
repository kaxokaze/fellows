# Fellows — launch and distribution notes

This is a working distribution plan for the current stage of the project. Fellows is a design-stage repository; it does not yet have a runnable implementation. Posts must preserve that distinction.

## Canonical links

- Repository: https://github.com/kaxokaze/fellows
- Project page (after GitHub Pages is enabled): https://kaxokaze.github.io/fellows/
- Architecture: https://github.com/kaxokaze/fellows/blob/main/docs/architecture/OVERVIEW.md
- Coordination protocol: https://github.com/kaxokaze/fellows/blob/main/docs/architecture/COORDINATION.md
- Evaluation plan: https://github.com/kaxokaze/fellows/blob/main/docs/evaluation/PLAN.md

## Positioning

Use this description consistently:

> Fellows is an open-source project exploring a peer-first collaboration runtime for independent AI agents. It separates peer reasoning from deterministic coordination, with shared project state, direct agent communication, task negotiation, controlled execution, and measurable evaluation.

Do not call Fellows a working platform, framework, SDK, or runtime until those components exist.

## Short post — X / Bluesky

I've started Fellows, an open-source project exploring a peer-first model for AI agents.

The idea: independent agents should be able to share project context, talk directly, challenge decisions, negotiate work, and coordinate execution—without one model acting as the permanent boss.

The hard parts are state consistency, task ownership, conflicts, permissions, and proving the approach is worth its cost.

It's at the design stage. I'm looking for engineers and researchers to critique the architecture and help shape a small, measurable prototype.

https://github.com/kaxokaze/fellows

## LinkedIn post

I'm working on an open-source project called Fellows.

The question behind it is straightforward: what would it take for independent AI agents to work together as peers on one project, rather than operating as subagents under a permanent lead model?

The difficult part isn't starting several model sessions. It's keeping them aligned: maintaining shared project state, resolving disagreements, assigning work without duplication, avoiding conflicting changes, and verifying the integrated result.

Fellows explores a peer-first reasoning layer backed by deterministic runtime infrastructure for state, task transitions, permissions, and recovery.

The project is currently at the architecture and research stage. There is no working runtime yet. The next step is a small three-agent software task, evaluated against single-agent and conventional orchestrated baselines.

I'm interested in feedback from people working on agent systems, distributed systems, developer infrastructure, and evaluation.

Project: https://github.com/kaxokaze/fellows

## Developer community post

**Title:** Fellows: exploring peer-first collaboration between independent AI agents

I'm exploring a design question for multi-agent software engineering.

A lot of agent systems can delegate work to multiple sessions. I'm interested in a different arrangement: independent agents that can communicate directly, share a project state, propose and challenge decisions, negotiate work, and review each other's output.

I don't think "more agents" is a useful goal by itself. Coordination has costs: stale context, duplicate work, conflicting edits, deadlocks, and extra inference spend. A peer system also still needs deterministic infrastructure for task ownership, permissions, event history, and recovery.

Fellows is a design-stage open-source project. I've published an architecture proposal, a coordination protocol draft, and an evaluation plan. The first prototype is intended to use three agents on one bounded software task and compare the result with a single agent and a conventional orchestrated team.

I'd value feedback on:
- whether the peer/control-plane boundary is sound;
- how task claims, decision finalization, and shared state should work;
- what existing systems or research I should study more closely;
- which task would make a fair first evaluation.

Repository: https://github.com/kaxokaze/fellows

## Recommended channels

### Suitable now

1. **Hugging Face Forums — Show and Tell:** share the architecture and ask for technical feedback. Keep the post focused on the design question, not a feature announcement.
   https://discuss.huggingface.co/c/show-and-tell/14

2. **Hugging Face Forums — Community Calls:** use only if asking for specific collaborators or a focused project review.
   https://discuss.huggingface.co/categories

3. **DEV Community:** publish a technical article about the coordination problem or the peer/control-plane design. Use relevant tags (up to four). The `#opensource` tag is not intended for simple project promotion; use a more appropriate tag such as `#ai`, `#agents`, or `#news` where it fits.
   https://dev.to/new

4. **GitHub Topics:** add accurate topics so developers can discover the repository by subject.
   https://github.com/topics/multi-agent
   https://github.com/topics/ai-agents

5. **Relevant technical communities:** participate in discussions about agent protocols, orchestration, shared state, and evaluation. Read each community's self-promotion rules before posting.

### Wait for a runnable prototype

- **Hacker News Show HN:** do not submit the landing page alone. The official guidelines say Show HN is for something people can try, not landing pages or reading material. Return with a runnable demo or CLI.
  https://news.ycombinator.com/showhn.html

- **Product Hunt:** wait until users can explore and use the product. Its guidance says pre-launch submissions may be removed and recommends waiting for a live product.
  https://help.producthunt.com/en/articles/484932-can-i-submit-an-unreleased-product

## Publishing checklist

- [ ] Enable GitHub Pages from the `main` branch and `/docs` folder.
- [ ] Set the GitHub repository description.
- [ ] Add accurate repository topics.
- [ ] Upload a custom social preview image (recommended 1280 × 640, under 1 MB).
- [ ] Publish one technical post and participate in its discussion.
- [ ] Ask for critique and reproducible feedback, not stars or upvotes.
- [ ] Keep a record of where each announcement was posted.
- [ ] Update the public status when implementation begins.

## Posting rules

- Never claim that proposed components already exist.
- Do not manufacture stars, votes, comments, users, or endorsements.
- Do not cross-post identical text to every community.
- Respect community rules and promotional limits.
- Reply to technical criticism with evidence or acknowledge uncertainty.
- Correct outdated claims when the project status changes.
