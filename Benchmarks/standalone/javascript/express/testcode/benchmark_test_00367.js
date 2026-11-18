// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00367(req, res) {
  const userInput = req.params.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.session.data = String(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00367 };
