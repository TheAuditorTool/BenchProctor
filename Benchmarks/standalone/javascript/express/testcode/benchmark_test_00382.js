// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00382(req, res) {
  const userInput = req.body.field || "";
  const data = `${userInput}`;
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00382 };
