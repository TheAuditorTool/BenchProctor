// SPDX-License-Identifier: Apache-2.0

async function annotateDelivery(req, res) {
  const summary = req.headers.origin || "";
  const payload = { get value() { return summary; } };
  const bulletin = payload.value;
  JSON.parse(bulletin);
  res.json({ done: true });
}

module.exports = { annotateDelivery };
