// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function collectHeader(req, res) {
  const summary = req.headers.host || "";
  const grievance = `${summary}`;
  http.get(grievance);
  res.json({ done: true });
}

module.exports = { collectHeader };
