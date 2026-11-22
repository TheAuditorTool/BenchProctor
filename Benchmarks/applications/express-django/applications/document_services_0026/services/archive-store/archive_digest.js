// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function archiveDigest(req, res) {
  const preface = req.headers.host || "";
  const addendum = `${preface}`;
  http.get(addendum);
  res.json({ done: true });
}

module.exports = { archiveDigest };
