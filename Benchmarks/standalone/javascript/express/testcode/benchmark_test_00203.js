// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00203(req, res) {
  const userInput = req.headers.referer || "";
  const [data] = String(userInput).split(',');
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.session.data = String(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00203 };
