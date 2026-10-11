#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render README.md from data/genui.json.

Single source of truth: data/genui.json.
Running with --check exits non-zero if the rendered file has drifted,
serving as our mandatory CI gate.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "README.md")


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def table(headers, rows, align=None):
    align = align or ["---"] * len(headers)
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(align) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def main():
    d = load("genui.json")
    layers = d["layers"]
    items = [i for l in layers for i in l["items"]]
    n_items = len(items)
    langs = sorted({i["language"] for i in items if i.get("language")})

    # Data-driven ecosystem tree (no hand-aligned ASCII: emoji are double-width).
    branches = layers[1:]
    tlines = ["```",
              f"Generative UI  ·  the model emits a UI spec, the client renders components",
              "│"]
    for idx, layer in enumerate(branches):
        branch = "└──" if idx == len(branches) - 1 else "├──"
        names = " · ".join(x["name"] for x in layer["items"])
        tlines.append(f"{branch} {layer['icon']} {layer['layer_name']}  →  {names}")
    tlines.append("```")
    eco_tree = "\n".join(tlines)

    L = []
    L.append(f"""<div align="center">

# awesome-generative-ui

**The ecosystem index for Generative UI — where an agent's output is a rendered interface, not a wall of text.**

Protocols, frameworks, component libraries, platform renderers, adapters, and real apps. {n_items} repositories across {len(langs)} languages — every entry a real, independently-usable project, verified live.

[![Sources Verified](https://img.shields.io/badge/CI-Sources%20Verified-brightgreen)](scripts/verify_sources.py)
[![Repos](https://img.shields.io/badge/repos-{n_items}-blue)](https://github.com/topics/generative-ui)
[![License](https://img.shields.io/badge/license-CC--BY--4.0-lightgrey.svg)](LICENSE)

> ⛔ **Not affiliated with any project listed.** Star counts are a live snapshot ({d['updated']}).

</div>

---

## 🤔 What is Generative UI?

{ d['model']['what'] }

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

{eco_tree}

---

## 📚 Full index

""")

    for i, layer in enumerate(layers, 1):
        L.append(f"### {layer['icon']} {i}. {layer['layer_name']}\n\n{layer['description']}\n\n")
        L.append(table(
            ["Project", "Role", "Lang", "★"],
            [[f"[{x['name']}]({x['url']})", x["role"], x.get("language") or "-", f"{x['stars']:,}"]
             for x in layer["items"]],
            ["---", "---", "---", "---:"]
        ))
        L.append("\n\n")

    L.append("""---

## 🔍 Detailed breakdown

""")

    for layer in layers:
        L.append(f"### {layer['icon']} {layer['layer_name']}\n\n")
        for x in layer["items"]:
            lic = f" · `{x['license']}`" if x.get("license") and x["license"] != "None" else ""
            L.append(f"""#### [{x['name']}]({x['url']}) · ★{x['stars']:,}

> **{x['role']}**{lic}

{x['what']}

- **Key capabilities:** {x['key_capabilities']}

""")
        L.append("---\n\n")

    L.append("""## ✅ Source verification

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
""")

    text = "\n".join(L)

    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if cur != text:
            sys.exit("README.md is stale — run: python3 scripts/gen_readme.py")
        print("README.md in sync")
        return

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {OUT} ({len(text):,} chars)")


if __name__ == "__main__":
    main()
