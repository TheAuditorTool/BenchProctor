// SPDX-License-Identifier: Apache-2.0

async function registerService(req, res) {
  const subtitle = req.params.id || "";
  let persona;
  const onInput = (v) => { persona = v; };
  onInput(subtitle);
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://audit-log:8000/append_audit", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ done: true });
}

module.exports = { registerService };
