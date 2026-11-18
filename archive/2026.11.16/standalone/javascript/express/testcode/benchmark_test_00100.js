// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00100(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = `${userInput}`;
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.session.data = String(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00100 };
