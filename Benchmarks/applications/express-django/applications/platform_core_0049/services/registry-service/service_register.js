// SPDX-License-Identifier: Apache-2.0

async function registerService(req, res) {
  const notice = req.body || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(notice);
  const persona = readInput();
  await fetch("http://config-service:8000/rollout_config", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ done: true });
}

module.exports = { registerService };
