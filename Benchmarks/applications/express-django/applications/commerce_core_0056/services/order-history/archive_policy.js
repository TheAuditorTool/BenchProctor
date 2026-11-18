// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function archivePolicy(req, res) {
  const citation = req.body || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(citation);
  const backorder = readInput();
  net.connect(80, new URL(String(backorder)).hostname);
  res.json({ done: true });
}

module.exports = { archivePolicy };
