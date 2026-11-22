// SPDX-License-Identifier: Apache-2.0

async function buildSnapshot(req, res) {
  const memo = req.headers.origin || "";
  const backorder = String(memo).slice(0, 200);
  JSON.parse(backorder);
  res.json({ done: true });
}

module.exports = { buildSnapshot };
