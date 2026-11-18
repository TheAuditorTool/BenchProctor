// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00477(req, res) {
  const userInput = req.params.id || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00477 };
