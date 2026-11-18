// SPDX-License-Identifier: Apache-2.0

async function publishQuota(req, res) {
  const passage = req.headers.origin || "";
  const payload = { get value() { return passage; } };
  const persona = payload.value;
  JSON.parse(persona);
  res.json({ done: true });
}

module.exports = { publishQuota };
