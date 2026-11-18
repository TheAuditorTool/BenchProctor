// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function collectSyndication(req, res) {
  const summary = req.body.payload || "";
  const addendum = String(summary).slice(0, 200);
  net.connect(80, new URL(String(addendum)).hostname);
  res.json({ done: true });
}

module.exports = { collectSyndication };
