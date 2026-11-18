// SPDX-License-Identifier: Apache-2.0

async function rotateSnapshot(req, res) {
  const footnote = req.body.field || "";
  const byline = decodeURIComponent(footnote);
  res.send("<div>" + byline + "</div>");
}

module.exports = { rotateSnapshot };
