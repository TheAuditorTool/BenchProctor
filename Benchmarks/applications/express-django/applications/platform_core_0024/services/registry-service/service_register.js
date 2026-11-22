// SPDX-License-Identifier: Apache-2.0

async function registerService(req, res) {
  const heading = req.headers.host || "";
  const handshake = `${heading}`;
  const _gateUrl = String(handshake);
  const _gateTarget = (() => { try { return new URL(_gateUrl); } catch (e) { return null; } })();
  if (!_gateTarget || !["http:", "https:"].includes(_gateTarget.protocol) || _gateTarget.username !== "" || _gateTarget.password !== "" || /[\x00-\x20\x7f\\]/.test(_gateUrl) || !["api.trustmesh.internal", "assets.trustcdn.io"].includes(_gateTarget.hostname)) { res.status(403).json({error:"host not allowed"}); return; }
  await fetch("http://quota-service:8000/enforce_quota", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: handshake})});
  res.json({ done: true });
}

module.exports = { registerService };
