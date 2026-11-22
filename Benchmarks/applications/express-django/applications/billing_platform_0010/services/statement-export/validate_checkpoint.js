// SPDX-License-Identifier: Apache-2.0

async function validateCheckpoint(req, res) {
  const headline = req.headers.origin || "";
  const remittance = String(headline).slice(0, 200);
  JSON.parse(remittance);
  res.json({ done: true });
}

module.exports = { validateCheckpoint };
