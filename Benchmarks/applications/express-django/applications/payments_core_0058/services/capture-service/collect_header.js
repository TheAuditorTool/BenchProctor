// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function collectHeader(req, res) {
  const caption = req.body || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(caption);
  const ledger = readInput();
  net.connect(80, new URL(String(ledger)).hostname);
  res.json({ done: true });
}

module.exports = { collectHeader };
