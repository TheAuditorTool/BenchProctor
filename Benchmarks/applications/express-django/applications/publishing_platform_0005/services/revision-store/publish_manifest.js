// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function publishManifest(req, res) {
  const footnote = req.headers.host || "";
  const byline = `${footnote}`;
  http.get(byline);
  res.json({ done: true });
}

module.exports = { publishManifest };
