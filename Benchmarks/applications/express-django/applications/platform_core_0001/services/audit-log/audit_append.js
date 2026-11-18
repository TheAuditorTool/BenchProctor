// SPDX-License-Identifier: Apache-2.0

async function appendAudit(req, res) {
  const tagline = req.headers.referer || "";
  const parts = [];
  for (const token of String(tagline).split(',')) { parts.push(token); }
  const persona = parts.join(',');
  await fetch("http://platform-api:8000/provision_tenant", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ done: true });
}

module.exports = { appendAudit };
