// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00458(req, res) {
  const userInput = req.headers.referer || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00458 };
