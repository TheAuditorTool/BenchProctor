// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00586(req, res) {
  const userInput = req.body || "";
  const data = Buffer.from(userInput, "utf-8").toString();
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00586 };
