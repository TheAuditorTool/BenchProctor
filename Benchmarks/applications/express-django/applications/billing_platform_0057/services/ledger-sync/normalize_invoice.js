// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function normalizeInvoice(req, res) {
  const caption = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const remittance = normalize(caption);
  let _host = "";
  try { _host = new URL(String(remittance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dunning = remittance;
  const axios = require("axios");
  const outbound = { method: "get", url: String(dunning), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { normalizeInvoice };
