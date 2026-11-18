// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00140(req, res) {
  const userInput = req.body || "";
  const data = `${userInput}`;
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.session.data = String(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00140 };
