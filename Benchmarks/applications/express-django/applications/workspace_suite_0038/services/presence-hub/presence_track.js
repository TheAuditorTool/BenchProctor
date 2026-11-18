// SPDX-License-Identifier: Apache-2.0

async function trackPresence(req, res) {
  const preface = req.body.payload || "";
  const _raw = preface;
  const remark = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://share-service:8000/grant_share", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: remark})});
  res.json({ done: true });
}

module.exports = { trackPresence };
