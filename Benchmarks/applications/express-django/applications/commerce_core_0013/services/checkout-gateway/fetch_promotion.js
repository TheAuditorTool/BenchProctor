// SPDX-License-Identifier: Apache-2.0

async function fetchPromotion(req, res) {
  const wording = req.headers.authorization || "";
  const backorder = Buffer.from(wording, "hex").toString();
  let _host = "";
  try { _host = new URL(String(backorder)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const voucher = backorder;
  const axios = require("axios");
  const outbound = { method: "get", url: String(voucher), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { fetchPromotion };
