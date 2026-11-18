// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00096(req, res) {
  const userInput = req.headers.origin || "";
  const data = userInput != null ? userInput : '';
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  req.session.data = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00096 };
