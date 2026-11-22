// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00135(req, res) {
  const userInput = req.query.id || "";
  const processed = ["true", "1", "yes", "on"].includes(String(userInput).toLowerCase()) ? "true" : "false";
  new Function("return (" + String(processed) + ");")();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00135 };
