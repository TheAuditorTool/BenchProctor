// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00198(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = userInput != null ? userInput : '';
  const emailMatch = String(data).match(/@([A-Za-z0-9.-]+)$/);
  if (!emailMatch) { res.status(400).json({ error: "not an email address" }); return; }
  const domain = emailMatch[1];
  res.json({ domain }); return;
}

module.exports = { BenchmarkTest00198 };
