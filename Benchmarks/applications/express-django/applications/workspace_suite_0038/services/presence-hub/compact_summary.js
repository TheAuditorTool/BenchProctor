// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function compactSummary(req, res) {
  const preface = req.headers["user-agent"] || "";
  http.get(preface);
  res.json({ done: true });
}

module.exports = { compactSummary };
