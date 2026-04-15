# Section 2: Using LLMs

**Course:** Python for AI Engineering (Towards AI Academy)
**Instructor:** Louis-François Bouchard
**Status:** Complete

---

## What This Section Covers

Section 2 has two lessons. The first introduces the three major LLM platforms and how they differ. The second covers prompt engineering: the techniques, the workflow, and the common mistakes.

---

## LLM Platforms: ChatGPT, Claude, and Gemini

### How LLMs Actually Work

LLMs don't think. They predict the next token based on patterns learned from training data. That distinction matters because it explains why outputs can sound confident and still be completely wrong. Verification is not optional.

The pipeline from raw model to the product you use looks like this:

Training data shapes model behavior. Post-training techniques like RLHF (Reinforcement Learning from Human Feedback) and fine-tuning refine tone, safety, and accuracy. Integrated tools like web search and code execution extend what the model can do. Agentic features build on top of all of that to enable autonomous, multi-step task completion.

### ChatGPT

One of the most widely used LLM platforms. Best for general-purpose coding, multimodal tasks, and complex reasoning via the o-series models. The most versatile option across task types.

### Claude

Built by Anthropic using a framework called Constitutional AI, which guides the model to be helpful, honest, and harmless. Best for structured content, long documents, and coding tasks that require reliability. Artifacts is a useful feature for iterative code and design work within a single window.

### Gemini

Google's platform. Leads on long-context processing, with a context window up to 2 million tokens. Also strongest for multimodal inputs across text, images, audio, and video.

### How to Choose

| Task | Recommended Platform |
|---|---|
| General coding and versatility | ChatGPT |
| Structured content and long documents | Claude |
| Large documents and multimodal input | Gemini |

All three platforms are converging rapidly and frequently replicate each other's features. The rankings above reflect current strengths, not permanent advantages.

### Privacy Note

Free tiers on most platforms allow prompt data to be used for model training. Paid tiers generally offer better protection. Review privacy settings before inputting anything sensitive.

---

## Prompt Engineering

### What Prompting Is

A prompt is the input or instruction you give to an AI model. The quality of your prompt directly determines the quality of the output. Vague prompts produce vague or wrong answers. The principle is simple: garbage in, garbage out.

Prompting is also iterative. The first output is rarely the best one. Treat a bad output as feedback, not failure, and use it to refine your next prompt.

### Core Techniques

**Zero-shot prompting**
Ask directly with no examples. Works well when the task is clear and unambiguous. Start here before adding complexity.

**Few-shot prompting**
Provide two to three examples within the prompt to show the model your preferred format or tone. Use this when zero-shot outputs miss the mark on structure or style.

**Chain-of-thought prompting**
Encouraging step-by-step reasoning can improve results on complex tasks like math, logic, and multi-part problems. A simple trigger like "Let's think step by step" is enough. Newer models often handle this internally without explicit instructions.

**Role prompting**
Assign a persona to the model at the start of your prompt. "You are an expert Python developer" implicitly sets the tone, vocabulary, and level of detail you can expect in return.

**Iterative prompting**
Draft a prompt, test the output, evaluate it against your goal, refine the prompt, and repeat. This is the core workflow, not a fallback.

### Prompting Workflow

```
DEFINE GOAL
↓
PROVIDE CONTEXT + CONSTRAINTS
↓
SPECIFY OUTPUT FORMAT
↓
TEST RESPONSE
↓
EVALUATE ACCURACY
↓
REFINE PROMPT
↓
REPEAT UNTIL SATISFIED
```

### Watch Out For

**Hallucinations**
LLMs confidently generate incorrect information when uncertain. This includes invented functions, wrong parameters, and fabricated facts. Enable web search when working with recent information or specific library syntax.

**System prompts**
Predefined instructions set by the system or platform that guide model behavior before you type anything. You won't always see them, but they shape every response.

### Note on Reasoning Models

For newer reasoning models like GPT o-series, the approach shifts slightly. Specify your goal, inputs, constraints, and desired output format. Skip scripted step-by-step instructions since the model handles its own reasoning internally.

---

## Key Takeaways

1. LLMs predict tokens, they don't think. Verification is always your responsibility.
2. Choose your platform based on the task: ChatGPT for versatility, Claude for structured output, Gemini for large documents and multimodal input.
3. Start with zero-shot prompts and add complexity only when needed.
4. Few-shot examples teach the model your preferred format faster than long instructions.
5. Chain-of-thought reduces errors on complex or multi-part tasks.
6. Role prompting shapes tone and expertise implicitly.
7. Treat every output as a draft. Iterate until it meets your standard.
8. Never input sensitive data without checking the platform's privacy policy first.

---

## Keywords and Definitions

| Term | Definition |
|---|---|
| Prompt | The input or instruction given to an AI model |
| Zero-shot prompting | Asking with no examples provided |
| Few-shot prompting | Providing examples within the prompt to guide output |
| Chain-of-thought (CoT) | Instructing the model to show reasoning steps before answering |
| Role prompting | Assigning a persona to shape tone and expertise |
| Hallucination | When a model generates confident but incorrect information |
| System prompt | Predefined instructions set by the system or platform that guide model behavior |
| Iterative prompting | Progressive refinement of prompts based on output evaluation |
| LLM | Large Language Model; AI trained to predict and generate text token by token |
| RLHF | Reinforcement Learning from Human Feedback; aligns model behavior with human preferences |
| Constitutional AI | Anthropic's framework guiding Claude to be helpful, honest, and harmless |
| AI Agent | An AI system that autonomously breaks down and executes multi-step tasks |
| Multimodal | Ability to process multiple input types such as text, image, audio, and video |
| Context window | The maximum amount of text a model can process at once |

---

## Resources

- [Blog: Prompting Is a Skill, Not a Trick](https://garretos.github.io/posts/prompting-is-a-skill/)
- NotebookLM notes (saved locally)
