// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00177(req, res) {
  const userInput = req.headers.authorization || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.session.data = String(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00177 };
