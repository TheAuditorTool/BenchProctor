// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00427(req, res) {
  const userInput = req.headers.authorization || "";
  const processed = ["true", "1", "yes", "on"].includes(String(userInput).toLowerCase()) ? "true" : "false";
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00427 };
