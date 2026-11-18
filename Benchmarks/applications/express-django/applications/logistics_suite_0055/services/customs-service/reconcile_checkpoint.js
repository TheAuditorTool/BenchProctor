// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function reconcileCheckpoint(req, res) {
  const heading = req.headers["x-custom-header"] || "";
  const _raw = heading;
  const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
  const fileContent = fs.readFileSync("/var/app/data/" + consignment, "utf8");
  res.send(fileContent);
}

module.exports = { reconcileCheckpoint };
