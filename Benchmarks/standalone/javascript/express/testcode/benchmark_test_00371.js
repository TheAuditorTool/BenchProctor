// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00371(req, res) {
  const userInput = req.headers.authorization || "";
  const [data] = String(userInput).split(',');
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00371 };
