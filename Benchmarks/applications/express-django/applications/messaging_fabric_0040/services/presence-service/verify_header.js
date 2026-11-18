// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function verifyHeader(req, res) {
  const preface = req.headers["x-custom-header"] || "";
  const _raw = preface;
  const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
  const fileContent = fs.readFileSync("/var/app/data/" + bulletin, "utf8");
  res.send(fileContent);
}

module.exports = { verifyHeader };
