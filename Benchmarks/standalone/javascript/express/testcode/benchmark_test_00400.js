// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00400(req, res) {
  const userInput = req.headers.referer || "";
  const processed = ["true", "1", "yes", "on"].includes(String(userInput).toLowerCase()) ? "true" : "false";
  req.session.data = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00400 };
