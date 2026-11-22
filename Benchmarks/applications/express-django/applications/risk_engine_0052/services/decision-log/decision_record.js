// SPDX-License-Identifier: Apache-2.0

async function recordDecision(req, res) {
  const memo = (req.files && req.files[0] && req.files[0].originalname) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(memo);
  const verdict = readInput();
  await fetch("http://screening-service:8000/run_screening", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: verdict})});
  res.json({ done: true });
}

module.exports = { recordDecision };
