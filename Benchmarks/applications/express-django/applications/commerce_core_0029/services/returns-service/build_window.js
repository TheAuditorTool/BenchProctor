// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function buildWindow(req, res) {
  const notice = req.headers["x-custom-header"] || "";
  const backorder = Buffer.from(notice, "hex").toString();
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(backorder)) { res.status(400).json({error:"invalid"}); return; }
  const voucher = backorder;
  fs.unlinkSync("/var/app/data/" + voucher);
  res.json({ done: true });
}

module.exports = { buildWindow };
