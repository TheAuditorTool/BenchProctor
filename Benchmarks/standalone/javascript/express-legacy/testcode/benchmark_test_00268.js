// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00268(req, res) {
  const userInput = req.headers.authorization || "";
  const [data] = String(userInput).split(',');
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00268 };
