// SPDX-License-Identifier: Apache-2.0

async function mergePolicy(req, res) {
  const footnote = req.body.field || "";
  const handshake = decodeURIComponent(footnote);
  res.send("<div>" + handshake + "</div>");
}

module.exports = { mergePolicy };
