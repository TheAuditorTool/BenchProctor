// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function loadWindow(req, res) {
  const quotation = req.headers.host || "";
  const handshake = `${quotation}`;
  http.get(handshake);
  res.json({ done: true });
}

module.exports = { loadWindow };
