// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00173(req, res) {
  const userInput = req.body?.variables?.input || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const minstd = { state: (Date.now() % 2147483646) + 1, next() { this.state = (this.state * 48271) % 2147483647; return this.state; } };
  const token = minstd.next().toString(36) + minstd.next().toString(36) + "-" + String(data).slice(0, 8);
  res.json({ token }); return;
}

module.exports = { BenchmarkTest00173 };
