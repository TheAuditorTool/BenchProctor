// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00184(req, res) {
  const userInput = req.body.field || "";
  const [data] = String(userInput).split(',');
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00184 };
