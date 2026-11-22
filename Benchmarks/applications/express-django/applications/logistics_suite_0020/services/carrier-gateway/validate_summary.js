// SPDX-License-Identifier: Apache-2.0

async function validateSummary(req, res) {
  const transcript = req.headers.origin || "";
  const consignment = String(transcript).slice(0, 200);
  JSON.parse(consignment);
  res.json({ done: true });
}

module.exports = { validateSummary };
