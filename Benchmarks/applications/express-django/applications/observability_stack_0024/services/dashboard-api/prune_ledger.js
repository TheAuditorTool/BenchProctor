// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function pruneLedger(req, res) {
  const summary = req.headers["user-agent"] || "";
  http.get(summary);
  res.json({ done: true });
}

module.exports = { pruneLedger };
