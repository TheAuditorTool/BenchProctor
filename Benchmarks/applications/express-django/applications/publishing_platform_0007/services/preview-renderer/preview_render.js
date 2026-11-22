// SPDX-License-Identifier: Apache-2.0

async function renderPreview(req, res) {
  const remark = req.params.id || "";
  globalThis.lastRequestValue = remark;
  const byline = globalThis.lastRequestValue;
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://revision-store:8000/save_revision", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
  res.json({ done: true });
}

module.exports = { renderPreview };
