// SPDX-License-Identifier: Apache-2.0

async function summarizeHeader(req, res) {
  const snippet = req.headers.authorization || "";
  const handshake = Buffer.from(snippet, "base64").toString();
  res.send("<div>" + handshake + "</div>");
}

module.exports = { summarizeHeader };
