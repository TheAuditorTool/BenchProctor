// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00041(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.session.data = String(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00041 };
