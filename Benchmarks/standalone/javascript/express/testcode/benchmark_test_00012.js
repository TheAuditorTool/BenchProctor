// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00012(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const data = userInput != null ? userInput : '';
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00012 };
