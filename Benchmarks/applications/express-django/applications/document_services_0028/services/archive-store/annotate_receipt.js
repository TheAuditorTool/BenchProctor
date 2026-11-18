// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function annotateReceipt(req, res) {
  const note = req.headers["user-agent"] || "";
  http.get(note);
  res.json({ done: true });
}

module.exports = { annotateReceipt };
