// SPDX-License-Identifier: Apache-2.0

async function buildBatch(req, res) {
  const note = req.headers.authorization || "";
  const handshake = Buffer.from(note, "base64").toString();
  res.send("<div>" + handshake + "</div>");
}

module.exports = { buildBatch };
