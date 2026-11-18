// SPDX-License-Identifier: Apache-2.0

async function rollDigest(req, res) {
  const paragraph = req.params.id || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(paragraph);
  const bulletin = readInput();
  await fetch("http://presence-service:8000/update_presence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ done: true });
}

module.exports = { rollDigest };
