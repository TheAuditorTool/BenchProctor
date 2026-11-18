// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00336(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00336 };
