// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function reconcileWindow(req, res) {
  const summary = req.headers.host || "";
  const addendum = `${summary}`;
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const byline = addendum;
  http.get(byline);
  res.json({ done: true });
}

module.exports = { reconcileWindow };
