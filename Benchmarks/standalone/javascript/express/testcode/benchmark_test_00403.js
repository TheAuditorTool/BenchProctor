// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00403(req, res) {
  const userInput = req.body || "";
  const data = String(userInput).slice(0, 200);
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.session.data = String(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00403 };
