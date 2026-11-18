// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00064(req, res) {
  const userInput = req.params.id || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  res.redirect(data);
}

module.exports = { BenchmarkTest00064 };
