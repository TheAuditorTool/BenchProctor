// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function fetchReceipt(req, res) {
  const note = req.headers.origin || "";
  const trim = (v) => String(v).trim();
  const byline = trim(note);
  let _host = "";
  try { _host = new URL(String(byline)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const addendum = byline;
  net.connect(80, new URL(String(addendum)).hostname);
  res.json({ done: true });
}

module.exports = { fetchReceipt };
