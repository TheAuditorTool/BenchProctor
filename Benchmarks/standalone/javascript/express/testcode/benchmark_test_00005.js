// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00005(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00005 };
