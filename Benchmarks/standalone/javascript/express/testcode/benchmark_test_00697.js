// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00697(req, res) {
  const userInput = req.headers["user-agent"] || "";
  req.session.data = String(userInput);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00697 };
