// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00197(req, res) {
  const userInput = req.headers.authorization || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const requested = boundedVal;
  if (!Number.isFinite(requested) || requested < 0 || requested > 1048576) { res.status(400).json({ error: "out of range" }); return; }
  const buf = Buffer.alloc(requested + 1);
  res.json({ allocated: buf.length }); return;
}

module.exports = { BenchmarkTest00197 };
