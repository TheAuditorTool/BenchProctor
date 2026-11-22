// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00292(req, res) {
  const userInput = req.headers.origin || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00292 };
