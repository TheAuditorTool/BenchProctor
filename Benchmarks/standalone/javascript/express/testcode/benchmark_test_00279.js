// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00279(req, res) {
  const userInput = req.body.payload || "";
  const [data] = String(userInput).split(',');
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00279 };
