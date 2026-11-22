// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00202(req, res) {
  const userInput = req.body || "";
  const data = String(userInput).slice(0, 200);
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  req.app.locals.announcement = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00202 };
