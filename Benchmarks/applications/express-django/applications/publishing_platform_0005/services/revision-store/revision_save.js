// SPDX-License-Identifier: Apache-2.0

async function saveRevision(req, res) {
  const footnote = req.params.id || "";
  const trim = (v) => String(v).trim();
  const byline = trim(footnote);
  await fetch("http://preview-renderer:8000/render_preview", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
  res.json({ done: true });
}

module.exports = { saveRevision };
