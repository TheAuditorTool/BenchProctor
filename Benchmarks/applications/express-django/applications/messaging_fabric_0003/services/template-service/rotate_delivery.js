// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function rotateDelivery(req, res) {
  const subject = req.cookies.session_token || "";
  const payload = { get value() { return subject; } };
  const bulletin = payload.value;
  http.get(bulletin);
  res.json({ done: true });
}

module.exports = { rotateDelivery };
