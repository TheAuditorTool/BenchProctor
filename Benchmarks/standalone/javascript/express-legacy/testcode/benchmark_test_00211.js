// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00211(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00211 };
