// SPDX-License-Identifier: Apache-2.0

async function normalizeBatch(req, res) {
  const memo = req.headers.origin || "";
  const verdict = String(memo).slice(0, 200);
  JSON.parse(verdict);
  res.json({ done: true });
}

module.exports = { normalizeBatch };
