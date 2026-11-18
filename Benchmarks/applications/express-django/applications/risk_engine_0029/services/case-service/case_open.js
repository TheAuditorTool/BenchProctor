// SPDX-License-Identifier: Apache-2.0

async function openCase(req, res) {
  const subject = req.headers.origin || "";
  const _input = String(subject);
  let grievance;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': grievance = _input.normalize('NFC'); break;
    default: grievance = _input; break;
  }
  const _gateHost = (() => { try { return new URL(String(grievance)).hostname; } catch (e) { return ""; } })();
  const _gateAddr = _gateHost ? (await require("dns").promises.lookup(_gateHost).catch(() => ({address: ""}))).address : "";
  const _gateBlocked = !_gateAddr || /^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.)/.test(_gateAddr) || _gateAddr === "::1" || /^f[cd]/i.test(_gateAddr) || /^fe80:/i.test(_gateAddr);
  if (_gateBlocked) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  await fetch("http://screening-service:8000/run_screening", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: grievance})});
  res.json({ done: true });
}

module.exports = { openCase };
