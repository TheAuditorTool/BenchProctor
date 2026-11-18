// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00339(req, res) {
  const userInput = req.body || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00339 };
