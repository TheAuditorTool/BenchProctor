// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00143(req, res) {
  const userInput = req.body || "";
  const data = Buffer.from(userInput, "utf-8").toString();
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00143 };
