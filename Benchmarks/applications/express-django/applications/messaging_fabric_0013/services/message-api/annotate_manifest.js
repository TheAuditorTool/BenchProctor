// SPDX-License-Identifier: Apache-2.0

async function annotateManifest(req, res) {
  const summary = req.body.field || "";
  const bulletin = decodeURIComponent(summary);
  res.send("<div>" + bulletin + "</div>");
}

module.exports = { annotateManifest };
