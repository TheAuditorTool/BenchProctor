// SPDX-License-Identifier: Apache-2.0

async function exportReport(req, res) {
  const phrase = req.headers.origin || "";
  const payload = { get value() { return phrase; } };
  const inquiry = payload.value;
  JSON.parse(inquiry);
  res.json({ done: true });
}

module.exports = { exportReport };
