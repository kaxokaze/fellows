# Roadmap

This is a working plan, not a list of completed features. Priorities may change as the design is tested.

## 1. Define the first experiment

- [ ] Review existing peer-based and orchestrated multi-agent systems.
- [ ] Write down what Fellows will and will not try to do.
- [ ] Choose one small software task with objective acceptance criteria.
- [ ] Define a single-agent baseline and a conventional multi-agent baseline.
- [ ] Set a model and cost budget for the experiment.

**Outcome:** a short design note and an experiment that can be repeated.

## 2. Build the smallest useful prototype

- [ ] Run three independent agents on one project.
- [ ] Give them a shared project state and a direct messaging mechanism.
- [ ] Let them propose, claim, and report work.
- [ ] Record decisions, dependencies, and unresolved questions.
- [ ] Keep tool access scoped and changes reviewable.
- [ ] Integrate the work and run the task's acceptance tests.

**Outcome:** a working example that shows how the agents coordinate, including where the approach fails.

## 3. Measure the result

- [ ] Run the same task with one agent.
- [ ] Run it with a conventional orchestrated multi-agent setup.
- [ ] Compare output quality, completion time, model usage, and integration problems.
- [ ] Repeat the experiment and publish the setup and results.

**Outcome:** evidence about when peer collaboration helps and when it does not.

## 4. Decide what to build next

Use the results to decide whether to improve coordination, shared memory, execution isolation, model selection, or the developer experience. Avoid adding features just to make the roadmap look bigger.
