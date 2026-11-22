// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00081(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = String(userInput).slice(0, 200);
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  req.session.data = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00081 };
