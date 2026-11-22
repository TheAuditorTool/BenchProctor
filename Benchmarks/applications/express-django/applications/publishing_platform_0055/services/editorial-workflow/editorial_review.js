// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function reviewEditorial(req, res) {
  const synopsis = req.headers["x-custom-header"] || "";
  const byline = nodeUtil.format("%s", synopsis);
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://preview-renderer:8000/render_preview", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
  res.json({ done: true });
}

module.exports = { reviewEditorial };
