<div align="center">

# awesome-generative-ui

**The ecosystem index for Generative UI — where an agent's output is a rendered interface, not a wall of text.**

Protocols, frameworks, component libraries, platform renderers, adapters, and real apps. 31 repositories across 5 languages — every entry a real, independently-usable project, verified live.

[![Sources Verified](https://img.shields.io/badge/CI-Sources%20Verified-brightgreen)](scripts/verify_sources.py)
[![Repos](https://img.shields.io/badge/repos-31-blue)](https://github.com/topics/generative-ui)
[![License](https://img.shields.io/badge/license-CC--BY--4.0-lightgrey.svg)](LICENSE)

> ⛔ **Not affiliated with any project listed.** Star counts are a live snapshot (2026-10-25).

</div>

---

## 🤔 What is Generative UI?

Generative UI is the pattern where an agent's output is not text but UI — the model emits a structured spec (often JSON or an event stream), and the client renders it with real components. It replaces 'here is a wall of markdown' with 'here is the actual widget you asked for'.

It is a **young, fast-moving category** (most of the projects below shipped in 2026) with real players — Vercel Labs, CopilotKit, Prefect, LangChain — and a standards race between AG-UI, A2UI, Open-JSON-UI, and MCP Apps. This list tracks all of it in one place.

---

## ⚡ Pick your entry point

| I want to… | Go to |
|---|---|
| Connect any agent backend to any frontend (the wire format) | [ag-ui](https://github.com/ag-ui-protocol/ag-ui) |
| Build on the dominant React framework | [CopilotKit](https://github.com/CopilotKit/CopilotKit) |
| Stream JSON and render it with my own components | [json-render](https://github.com/vercel-labs/json-render) |
| Let the model pick from my registered components | [tambo](https://github.com/tambo-ai/tambo) |
| Build on an open standard + DSL | [openui](https://github.com/thesysdev/openui) |
| Get Tailwind components shaped for AI UIs | [langui](https://github.com/CommandCodeAI/langui) |
| Build a React chat surface | [assistant-ui](https://github.com/assistant-ui/assistant-ui) |
| Render on iOS / Android / HarmonyOS | [AGenUI](https://github.com/AGenUI/AGenUI) |
| Render in Vue | [a2ui-vue](https://github.com/shawnwang15/a2ui-vue) |
| Render in Angular | [ngx-json-render](https://github.com/shteynu/ngx-json-render) |
| Render in the terminal | [termite](https://github.com/shobrook/termite) |
| Wire it into LangGraph | [langgraphjs-gen-ui-examples](https://github.com/langchain-ai/langgraphjs-gen-ui-examples) |
| Use the Vercel AI SDK | [ai-sdk-preview-rsc-genui](https://github.com/vercel-labs/ai-sdk-preview-rsc-genui) |
| See a full production app | [morphic](https://github.com/miurla/morphic) |

---

## 🗺️ Map of the ecosystem

```
Generative UI  ·  the model emits a UI spec, the client renders components
│
├── 🏗️ Frameworks & SDKs  →  CopilotKit · json-render · tambo · OpenIntelligentUI · prefab · flama · threadplane · moi
├── 🧩 Component Libraries  →  assistant-ui · langui · flutter_chat_ui
├── 🖥️ Platform Renderers  →  AGenUI · A2UI-Android · a2ui-vue · ngx-json-render · termite
├── 🔌 Framework Adapters & Examples  →  gemini-chatbot · langgraphjs-gen-ui-examples · gen-ui-python · gen-ui · ai-sdk-preview-rsc-genui
└── 🎬 Apps & Demos  →  morphic · cofounder · pi-generative-ui · financial-agent-ui · partialupdate · MAIC-UI
```

---

## 📚 Full index


### 📐 1. Protocols & Standards

The wire formats. An agent backend emits these; any conforming renderer draws them. This is the layer that makes generative UI portable across frameworks — and it is why adapters and renderers below can be written by anyone.


| Project | Role | Lang | ★ |
|---|---|---|---:|
| [ag-ui](https://github.com/ag-ui-protocol/ag-ui) | Protocol | TypeScript | 16,455 |
| [openui](https://github.com/thesysdev/openui) | Standard · DSL | TypeScript | 10,718 |
| [a2ui-sdk](https://github.com/easyops-cn/a2ui-sdk) | Protocol SDK | TypeScript | 39 |
| [generative-ui](https://github.com/CopilotKit/generative-ui) | Reference examples | - | 848 |



### 🏗️ 2. Frameworks & SDKs

End-to-end frameworks that own the loop from model output to rendered UI. Pick by stack and by how much control you want over which component renders.


| Project | Role | Lang | ★ |
|---|---|---|---:|
| [CopilotKit](https://github.com/CopilotKit/CopilotKit) | Framework · React/Angular/Mobile | TypeScript | 37,940 |
| [json-render](https://github.com/vercel-labs/json-render) | Framework · React | TypeScript | 18,615 |
| [tambo](https://github.com/tambo-ai/tambo) | SDK · React | TypeScript | 11,188 |
| [OpenIntelligentUI](https://github.com/CopilotKit/OpenIntelligentUI) | Framework | TypeScript | 2,643 |
| [prefab](https://github.com/PrefectHQ/prefab) | Framework | HTML | 742 |
| [flama](https://github.com/vortico/flama) | Framework · Python | Python | 301 |
| [threadplane](https://github.com/cacheplane/threadplane) | Infrastructure | TypeScript | 305 |
| [moi](https://github.com/molefrog/moi) | Workspace | TypeScript | 183 |



### 🧩 3. Component Libraries

The primitives you compose into an agent UI. Not full frameworks — these are the chat shells, message parts, and tool-call renders you build on.


| Project | Role | Lang | ★ |
|---|---|---|---:|
| [assistant-ui](https://github.com/assistant-ui/assistant-ui) | Library · React | TypeScript | 12,480 |
| [langui](https://github.com/CommandCodeAI/langui) | Library · Tailwind | HTML | 3,144 |
| [flutter_chat_ui](https://github.com/flyerhq/flutter_chat_ui) | Library · Flutter | Dart | 2,360 |



### 🖥️ 4. Platform Renderers

Same protocol, different surface. These projects render agent-emitted UI on a specific platform — mobile, a JS framework, or the terminal.


| Project | Role | Lang | ★ |
|---|---|---|---:|
| [AGenUI](https://github.com/AGenUI/AGenUI) | Renderer · Mobile | C++ | 1,192 |
| [A2UI-Android](https://github.com/lmee/A2UI-Android) | Renderer · Android | TypeScript | 77 |
| [a2ui-vue](https://github.com/shawnwang15/a2ui-vue) | Renderer · Vue 3 | TypeScript | 98 |
| [ngx-json-render](https://github.com/shteynu/ngx-json-render) | Renderer · Angular | TypeScript | 4 |
| [termite](https://github.com/shobrook/termite) | Renderer · Terminal | Python | 420 |



### 🔌 5. Framework Adapters & Examples

Reference implementations that wire generative UI into a specific agent framework. Copy the shape, not just the idea.


| Project | Role | Lang | ★ |
|---|---|---|---:|
| [gemini-chatbot](https://github.com/vercel-labs/gemini-chatbot) | Starter · Vercel AI SDK | TypeScript | 1,353 |
| [langgraphjs-gen-ui-examples](https://github.com/langchain-ai/langgraphjs-gen-ui-examples) | Examples · LangGraph JS | TypeScript | 400 |
| [gen-ui-python](https://github.com/bracesproul/gen-ui-python) | Examples · LangChain Python | TypeScript | 388 |
| [gen-ui](https://github.com/bracesproul/gen-ui) | Examples · LangChain JS | TypeScript | 292 |
| [ai-sdk-preview-rsc-genui](https://github.com/vercel-labs/ai-sdk-preview-rsc-genui) | Examples · React Server Components | TypeScript | 385 |



### 🎬 6. Apps & Demos

Finished products and runnable demos where the UI is authored by a model — the fastest way to see what generative UI actually feels like.


| Project | Role | Lang | ★ |
|---|---|---|---:|
| [morphic](https://github.com/miurla/morphic) | App · AI search | TypeScript | 9,159 |
| [cofounder](https://github.com/nraiden/cofounder) | App · full-stack | TypeScript | 6,645 |
| [pi-generative-ui](https://github.com/Michaelliv/pi-generative-ui) | Demo | TypeScript | 1,162 |
| [financial-agent-ui](https://github.com/virattt/financial-agent-ui) | Demo · finance | TypeScript | 793 |
| [partialupdate](https://github.com/philholden/partialupdate) | Demo · multi-user | TypeScript | 254 |
| [MAIC-UI](https://github.com/THU-MAIC/MAIC-UI) | Demo · education | Python | 175 |



---

## 🔍 Detailed breakdown


### 📐 Protocols & Standards


#### [ag-ui](https://github.com/ag-ui-protocol/ag-ui) · ★16,455

> **Protocol** · `MIT`

The Agent-User Interaction Protocol — a transport-agnostic event stream connecting any agent backend to any frontend. Reference spec with Python and TypeScript SDKs.

- **Key capabilities:** Event-stream spec · Python + TS SDKs


#### [openui](https://github.com/thesysdev/openui) · ★10,718

> **Standard · DSL** · `MIT`

An open standard and DSL for generative UI: the model emits OpenUI Lang, any conforming renderer draws it. Ships with a component library and renderers.

- **Key capabilities:** OpenUI Lang DSL · framework-agnostic


#### [a2ui-sdk](https://github.com/easyops-cn/a2ui-sdk) · ★39

> **Protocol SDK** · `Apache-2.0`

TypeScript SDK for the A2UI protocol — agent-to-UI messages that render as native components on any surface.

- **Key capabilities:** A2UI · TypeScript


#### [generative-ui](https://github.com/CopilotKit/generative-ui) · ★848

> **Reference examples**

Official side-by-side examples of all three generative-UI methods: AG-UI, A2UI/Open-JSON-UI, and MCP Apps.

- **Key capabilities:** AG-UI · A2UI · MCP Apps


---


### 🏗️ Frameworks & SDKs


#### [CopilotKit](https://github.com/CopilotKit/CopilotKit) · ★37,940

> **Framework · React/Angular/Mobile** · `MIT`

The frontend stack for agents and generative UI — React, Angular, mobile, and Slack surfaces, built on AG-UI.

- **Key capabilities:** React/Angular · AG-UI · generative UI


#### [json-render](https://github.com/vercel-labs/json-render) · ★18,615

> **Framework · React** · `Apache-2.0`

Vercel Labs' generative UI framework: the model streams JSON, the client renders it with your own components. Third-party renderers already exist for other frameworks.

- **Key capabilities:** streamed JSON · bring-your-own components


#### [tambo](https://github.com/tambo-ai/tambo) · ★11,188

> **SDK · React** · `MIT`

Generative UI SDK for React — the agent decides which of your registered components to render, and with what props.

- **Key capabilities:** React · component selection


#### [OpenIntelligentUI](https://github.com/CopilotKit/OpenIntelligentUI) · ★2,643

> **Framework** · `MIT`

Open-source generative UI framework.

- **Key capabilities:** generative UI


#### [prefab](https://github.com/PrefectHQ/prefab) · ★742

> **Framework** · `Apache-2.0`

A generative UI framework from Prefect that even humans can use — declarative UI the model composes.

- **Key capabilities:** declarative · model-composed


#### [flama](https://github.com/vortico/flama) · ★301

> **Framework · Python** · `Apache-2.0`

A production framework for predictive and generative AI, with a built-in UI layer.

- **Key capabilities:** Python · production


#### [threadplane](https://github.com/cacheplane/threadplane) · ★305

> **Infrastructure** · `MIT`

The open-source thread-plane for agents: chat, durable threads, and generative UI in one runtime.

- **Key capabilities:** durable threads


#### [moi](https://github.com/molefrog/moi) · ★183

> **Workspace** · `NOASSERTION`

Agent-agnostic generative UI workspace — give any agent a shared canvas.

- **Key capabilities:** agent-agnostic canvas


---


### 🧩 Component Libraries


#### [assistant-ui](https://github.com/assistant-ui/assistant-ui) · ★12,480

> **Library · React** · `MIT`

TypeScript/React library for AI chat — streaming-safe primitives for messages, tool calls, and generated parts.

- **Key capabilities:** React · streaming chat primitives


#### [langui](https://github.com/CommandCodeAI/langui) · ★3,144

> **Library · Tailwind** · `MIT`

Open-source Tailwind components tailored for AI interfaces — chat, tool calls, and generated UI.

- **Key capabilities:** Tailwind · AI-shaped components


#### [flutter_chat_ui](https://github.com/flyerhq/flutter_chat_ui) · ★2,360

> **Library · Flutter** · `Apache-2.0`

Free and open-source chat SDK for Flutter — fast, real-time, cross-platform chat UI.

- **Key capabilities:** Flutter · cross-platform


---


### 🖥️ Platform Renderers


#### [AGenUI](https://github.com/AGenUI/AGenUI) · ★1,192

> **Renderer · Mobile** · `Apache-2.0`

Native A2UI renderer for iOS, Android and HarmonyOS — high-performance streaming generative UI on mobile.

- **Key capabilities:** iOS/Android/HarmonyOS · streaming


#### [A2UI-Android](https://github.com/lmee/A2UI-Android) · ★77

> **Renderer · Android** · `Apache-2.0`

Production-ready Jetpack Compose renderer for the A2UI protocol.

- **Key capabilities:** Jetpack Compose


#### [a2ui-vue](https://github.com/shawnwang15/a2ui-vue) · ★98

> **Renderer · Vue 3** · `MIT`

Vue 3 implementation of the A2UI protocol.

- **Key capabilities:** Vue 3


#### [ngx-json-render](https://github.com/shteynu/ngx-json-render) · ★4

> **Renderer · Angular** · `Apache-2.0`

Generative UI for Angular: a json-render renderer that streams and renders the JSON UI spec.

- **Key capabilities:** Angular · json-render


#### [termite](https://github.com/shobrook/termite) · ★420

> **Renderer · Terminal** · `Apache-2.0`

Generative UI in your terminal — render rich agent output as a TUI instead of plain text.

- **Key capabilities:** terminal UI


---


### 🔌 Framework Adapters & Examples


#### [gemini-chatbot](https://github.com/vercel-labs/gemini-chatbot) · ★1,353

> **Starter · Vercel AI SDK** · `NOASSERTION`

Build your own generative UI chatbot with the Vercel AI SDK and Gemini.

- **Key capabilities:** chatbot starter


#### [langgraphjs-gen-ui-examples](https://github.com/langchain-ai/langgraphjs-gen-ui-examples) · ★400

> **Examples · LangGraph JS** · `MIT`

A collection of generative UI agents written with LangGraph.js.

- **Key capabilities:** LangGraph.js


#### [gen-ui-python](https://github.com/bracesproul/gen-ui-python) · ★388

> **Examples · LangChain Python**

Generative UI web application built with LangChain in Python.

- **Key capabilities:** LangChain Python


#### [gen-ui](https://github.com/bracesproul/gen-ui) · ★292

> **Examples · LangChain JS**

Generative UI web application built with LangChain.js.

- **Key capabilities:** LangChain.js


#### [ai-sdk-preview-rsc-genui](https://github.com/vercel-labs/ai-sdk-preview-rsc-genui) · ★385

> **Examples · React Server Components**

Generative UI with React Server Components and the Vercel AI SDK.

- **Key capabilities:** RSC · AI SDK


---


### 🎬 Apps & Demos


#### [morphic](https://github.com/miurla/morphic) · ★9,159

> **App · AI search** · `Apache-2.0`

An AI-powered search engine with a generative UI — answers rendered as interactive components, not walls of text.

- **Key capabilities:** AI search · generative answers


#### [cofounder](https://github.com/nraiden/cofounder) · ★6,645

> **App · full-stack** · `MIT`

AI-generated apps — full stack plus generative UI.

- **Key capabilities:** full-stack generation


#### [pi-generative-ui](https://github.com/Michaelliv/pi-generative-ui) · ★1,162

> **Demo**

Claude.ai's generative UI — reverse-engineered and rebuilt for self-hosting.

- **Key capabilities:** reverse-engineered demos


#### [financial-agent-ui](https://github.com/virattt/financial-agent-ui) · ★793

> **Demo · finance**

A financial agent paired with a generative UI.

- **Key capabilities:** finance agent


#### [partialupdate](https://github.com/philholden/partialupdate) · ★254

> **Demo · multi-user** · `MIT`

Generative UI in multi-user chat — a bot that edits the shared UI as it responds.

- **Key capabilities:** multi-user editing


#### [MAIC-UI](https://github.com/THU-MAIC/MAIC-UI) · ★175

> **Demo · education**

Making interactive courseware with generative UI.

- **Key capabilities:** interactive courseware


---


## ✅ Source verification

Every repository in this list is checked for reachability by CI:

```bash
python3 scripts/verify_sources.py
```

The gate fails loudly if a cited source goes dark, so the index cannot silently rot.

---

<div align="center">

**Data** — [`data/genui.json`](data/genui.json) · **Validator** — [`scripts/verify_sources.py`](scripts/verify_sources.py)

<sub>README.md is generated from data/genui.json. Edit the JSON, not this file.</sub>

</div>
