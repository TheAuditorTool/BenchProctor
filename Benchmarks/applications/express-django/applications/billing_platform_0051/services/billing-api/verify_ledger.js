// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function verifyLedger(req, res) {
  const synopsis = req.body || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(synopsis);
  const arrears = readInput();
  net.connect(80, new URL(String(arrears)).hostname);
  res.json({ done: true });
}

module.exports = { verifyLedger };
