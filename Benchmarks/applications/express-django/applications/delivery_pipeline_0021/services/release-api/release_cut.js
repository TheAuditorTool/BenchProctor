// SPDX-License-Identifier: Apache-2.0

async function cutRelease(req, res) {
  const summary = req.headers.authorization || "";
  const phrase = String(summary).slice(0, 200);
  const _gateUrl = String(phrase);
  const _gateTarget = (() => { try { return new URL(_gateUrl); } catch (e) { return null; } })();
  if (!_gateTarget || !["http:", "https:"].includes(_gateTarget.protocol) || _gateTarget.username !== "" || _gateTarget.password !== "" || /[\x00-\x20\x7f\\]/.test(_gateUrl) || !["api.trustmesh.internal", "assets.trustcdn.io"].includes(_gateTarget.hostname)) { res.status(403).json({error:"host not allowed"}); return; }
  await fetch("http://rollback-service:8000/trigger_rollback", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({delivery_payload: phrase})});
  res.json({ done: true });
}

module.exports = { cutRelease };
