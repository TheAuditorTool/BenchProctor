// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00170(req, res) {
  const userInput = req.body.payload || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  new Function("return (" + String(parsedNum) + ");")();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00170 };
