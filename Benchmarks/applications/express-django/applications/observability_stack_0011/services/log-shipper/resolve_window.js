// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function resolveWindow(req, res) {
  const caption = req.body.payload || "";
  const gauge = String(caption).slice(0, 200);
  net.connect(80, new URL(String(gauge)).hostname);
  res.json({ done: true });
}

module.exports = { resolveWindow };
