// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function compactChannel(req, res) {
  const footnote = req.query.id || "";
  const formData = Object.freeze({ payload: footnote });
  const bulletin = formData.payload;
  http.get(bulletin);
  res.json({ done: true });
}

module.exports = { compactChannel };
