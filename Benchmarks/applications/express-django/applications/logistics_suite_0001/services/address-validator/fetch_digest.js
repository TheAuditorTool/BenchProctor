// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function fetchDigest(req, res) {
  const quotation = process.env.SHIPPING_INPUT_0001 || "";
  const payload = { get value() { return quotation; } };
  const parcel = payload.value;
  const resolved = path.resolve("/var/app/data", parcel);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const consignment = resolved;
  fs.unlinkSync(consignment);
  res.json({ done: true });
}

module.exports = { fetchDigest };
