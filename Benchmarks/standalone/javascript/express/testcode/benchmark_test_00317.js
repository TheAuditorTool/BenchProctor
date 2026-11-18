// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00317(req, res) {
  const userInput = req.body || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.session.data = String(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00317 };
