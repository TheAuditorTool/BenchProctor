// SPDX-License-Identifier: Apache-2.0

async function attachAsset(req, res) {
  const heading = req.body?.field || "";
  let addendum;
  try { addendum = JSON.parse(heading).value || heading; }
  catch (e) { addendum = heading; }
  await fetch("http://preview-renderer:8000/render_preview", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: addendum})});
  res.json({ done: true });
}

module.exports = { attachAsset };
