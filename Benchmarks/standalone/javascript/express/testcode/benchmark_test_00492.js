// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00492(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00492 };
