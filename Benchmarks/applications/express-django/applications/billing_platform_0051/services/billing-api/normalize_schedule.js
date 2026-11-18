// SPDX-License-Identifier: Apache-2.0

async function normalizeSchedule(req, res) {
  const synopsis = req.headers.origin || "";
  const payload = { get value() { return synopsis; } };
  const arrears = payload.value;
  JSON.parse(arrears);
  res.json({ done: true });
}

module.exports = { normalizeSchedule };
