// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00202(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  Object.assign(req.session, { data: String(data), expiresAt: Date.now() + 900000 });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00202 };
