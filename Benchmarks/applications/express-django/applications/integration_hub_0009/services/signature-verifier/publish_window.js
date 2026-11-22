// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function publishWindow(req, res) {
  const heading = req.headers.host || "";
  const handshake = `${heading}`;
  http.get(handshake);
  res.json({ done: true });
}

module.exports = { publishWindow };
