// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00014(req, res) {
  const userInput = req.body || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00014 };
