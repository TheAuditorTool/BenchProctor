// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function validateBundle(req, res) {
  const excerpt = req.headers["x-forwarded-for"] || "";
  const trim = (v) => String(v).trim();
  const gauge = trim(excerpt);
  let _host = "";
  try { _host = new URL(String(gauge)).hostname; } catch (e) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const _addr = (await require("dns").promises.lookup(_host)).address;
  if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const cohort = gauge;
  http.get(cohort);
  res.json({ done: true });
}

module.exports = { validateBundle };
