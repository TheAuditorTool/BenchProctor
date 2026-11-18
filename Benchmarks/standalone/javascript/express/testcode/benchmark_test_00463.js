// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00463(req, res) {
  const userInput = req.body.field || "";
  const data = decodeURIComponent(userInput);
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00463 };
