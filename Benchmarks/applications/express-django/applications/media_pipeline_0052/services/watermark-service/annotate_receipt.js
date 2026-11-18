// SPDX-License-Identifier: Apache-2.0

async function annotateReceipt(req, res) {
  const tagline = req.body.field || "";
  const rendition = decodeURIComponent(tagline);
  res.send("<div>" + rendition + "</div>");
}

module.exports = { annotateReceipt };
