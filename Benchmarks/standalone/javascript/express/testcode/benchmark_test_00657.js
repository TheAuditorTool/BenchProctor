// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00657(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = Buffer.from(userInput, "hex").toString();
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.session.data = String(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00657 };
