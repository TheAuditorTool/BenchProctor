// SPDX-License-Identifier: Apache-2.0

async function attachAsset(req, res) {
  const summary = req.headers["x-custom-header"] || "";
  const _raw = summary;
  const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://article-api:8000/draft_article", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: addendum})});
  res.json({ done: true });
}

module.exports = { attachAsset };
