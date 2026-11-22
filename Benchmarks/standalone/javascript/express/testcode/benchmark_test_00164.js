// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00164(req, res) {
  const userInput = req.headers.host || "";
  const data = userInput != null ? userInput : '';
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  Object.assign(req.session, { data: String(processed), expiresAt: Date.now() + 900000 });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00164 };
