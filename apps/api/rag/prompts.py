from jinja2 import Template

AUGMENTED_PROMPT = Template("""\
[CONTEXT — top retrieved Knowledge Pack chunks]
{% for ch in chunks -%}
(id: {{ ch.doc_id }} — {{ ch.section }})
{{ ch.content | replace("\n", " ") }}
---
{% endfor -%}
-- END CONTEXT --

You are DB-Design Copilot.
Use ONLY the CONTEXT above. If essential info is missing, say "Insufficient context" and propose up to 3 targeted questions.
Cite section ids (doc_id) when you state definitions or rules.

User task:
{{ user_query }}
""")
