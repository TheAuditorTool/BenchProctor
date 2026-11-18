// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function annotateAllocation(req, res) {
  const phrase = req.headers.host || "";
  const backorder = `${phrase}`;
  http.get(backorder);
  res.json({ done: true });
}

module.exports = { annotateAllocation };
