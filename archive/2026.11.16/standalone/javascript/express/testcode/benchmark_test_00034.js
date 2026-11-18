// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00034(req, res) {
  const userInput = req.params.id || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00034 };
