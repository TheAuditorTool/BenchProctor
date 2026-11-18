// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function buildSnapshot(req, res) {
  const notice = req.headers["user-agent"] || "";
  http.get(notice);
  res.json({ done: true });
}

module.exports = { buildSnapshot };
