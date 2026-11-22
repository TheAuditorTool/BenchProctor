// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00294(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const quantity = boundedVal;
  if (!Number.isInteger(quantity) || quantity < 1 || quantity > 1000) { res.status(400).json({ error: "quantity out of range" }); return; }
  const totalCents = Math.imul(quantity, 1999);
  res.json({ quantity, totalCents }); return;
}

module.exports = { BenchmarkTest00294 };
