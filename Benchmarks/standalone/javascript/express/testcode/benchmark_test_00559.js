// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00559(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = String(userInput).slice(0, 200);
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00559 };
