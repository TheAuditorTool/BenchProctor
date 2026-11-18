// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function normalizeSnapshot(req, res) {
  const summary = req.headers.host || "";
  const bulletin = `${summary}`;
  http.get(bulletin);
  res.json({ done: true });
}

module.exports = { normalizeSnapshot };
