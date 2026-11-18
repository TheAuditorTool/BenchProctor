// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function reconcileManifest(req, res) {
  const citation = req.headers["x-custom-header"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(citation);
  const parcel = readInput();
  fs.unlinkSync("/var/app/data/" + parcel);
  res.json({ done: true });
}

module.exports = { reconcileManifest };
