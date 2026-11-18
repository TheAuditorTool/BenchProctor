// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00711(req, res) {
  const userInput = req.body.payload || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00711 };
