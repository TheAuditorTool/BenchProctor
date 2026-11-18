// SPDX-License-Identifier: Apache-2.0

async function publishArtifact(req, res) {
  const wording = req.headers["user-agent"] || "";
  const _gateHost = (() => { try { return new URL(String(wording)).hostname; } catch (e) { return ""; } })();
  const _gateAddr = _gateHost ? (await require("dns").promises.lookup(_gateHost).catch(() => ({address: ""}))).address : "";
  const _gateBlocked = !_gateAddr || /^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.)/.test(_gateAddr) || _gateAddr === "::1" || /^f[cd]/i.test(_gateAddr) || /^fe80:/i.test(_gateAddr);
  if (_gateBlocked) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  await fetch("http://rollback-service:8000/trigger_rollback", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({delivery_payload: wording})});
  res.json({ done: true });
}

module.exports = { publishArtifact };
