// SPDX-License-Identifier: Apache-2.0

async function runSettlement(req, res) {
  const remark = req.body || "";
  const remittance = String(remark).split(/[ \t]+/).join(" ");
  const _gateHost = (() => { try { return new URL(String(remittance)).hostname; } catch (e) { return ""; } })();
  const _gateAddr = _gateHost ? (await require("dns").promises.lookup(_gateHost).catch(() => ({address: ""}))).address : "";
  const _gateBlocked = !_gateAddr || /^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.)/.test(_gateAddr) || _gateAddr === "::1" || /^f[cd]/i.test(_gateAddr) || /^fe80:/i.test(_gateAddr);
  if (_gateBlocked) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  await fetch("http://payment-gateway:8000/capture_payment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: remittance})});
  res.json({ done: true });
}

module.exports = { runSettlement };
