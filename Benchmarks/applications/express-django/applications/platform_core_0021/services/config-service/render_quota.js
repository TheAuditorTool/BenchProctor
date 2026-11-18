// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function renderQuota(req, res) {
  const excerpt = req.headers["user-agent"] || "";
  http.get(excerpt);
  res.json({ done: true });
}

module.exports = { renderQuota };
