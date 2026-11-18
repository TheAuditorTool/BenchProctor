// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00655(req, res) {
  const userInput = req.cookies.session_token || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00655 };
