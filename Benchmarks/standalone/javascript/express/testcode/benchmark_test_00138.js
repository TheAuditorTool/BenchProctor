// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00138(req, res) {
  const userInput = req.headers.authorization || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  req.app.locals.announcement = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00138 };
