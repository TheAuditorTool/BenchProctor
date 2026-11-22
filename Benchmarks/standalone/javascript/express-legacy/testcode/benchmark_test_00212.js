// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00212(req, res) {
  const userInput = req.body.field || "";
  const emailMatch = String(userInput).match(/@([A-Za-z0-9.-]+)$/);
  if (!emailMatch) { res.status(400).json({ error: "not an email address" }); return; }
  const domain = emailMatch[1];
  res.json({ domain }); return;
}

module.exports = { BenchmarkTest00212 };
