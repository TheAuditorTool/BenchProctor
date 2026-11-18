// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function validateProfile(req, res) {
  const synopsis = req.body || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(synopsis);
  const handshake = readInput();
  net.connect(80, new URL(String(handshake)).hostname);
  res.json({ done: true });
}

module.exports = { validateProfile };
