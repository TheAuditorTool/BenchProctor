// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00248(req, res) {
  const userInput = req.cookies.session_token || "";
  const processed = ["true", "1", "yes", "on"].includes(String(userInput).toLowerCase()) ? "true" : "false";
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00248 };
