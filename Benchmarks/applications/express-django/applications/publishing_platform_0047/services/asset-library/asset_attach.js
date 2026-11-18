// SPDX-License-Identifier: Apache-2.0

async function attachAsset(req, res) {
  const synopsis = req.params.id || "";
  const parts = [];
  for (const token of String(synopsis).split(',')) { parts.push(token); }
  const byline = parts.join(',');
  await fetch("http://syndication-feed:8000/push_syndication", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
  res.json({ done: true });
}

module.exports = { attachAsset };
