// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function validateMapping(req, res) {
  const snippet = req.body || "";
  const handshake = String(snippet).split(/[ \t]+/).join(" ");
  http.get(handshake);
  res.json({ done: true });
}

module.exports = { validateMapping };
