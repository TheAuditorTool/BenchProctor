// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function validateManifest(req, res) {
  const subject = req.headers["x-custom-header"] || "";
  const voucher = Buffer.from(subject, "hex").toString();
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(voucher)) { res.status(400).json({error:"invalid"}); return; }
  const backorder = voucher;
  fs.unlinkSync("/var/app/data/" + backorder);
  res.json({ done: true });
}

module.exports = { validateManifest };
