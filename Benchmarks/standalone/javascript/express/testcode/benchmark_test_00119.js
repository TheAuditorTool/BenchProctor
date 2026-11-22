// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00119(req, res) {
  const userInput = req.body?.variables?.input || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  new Function("return (" + String(processed) + ");")();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00119 };
