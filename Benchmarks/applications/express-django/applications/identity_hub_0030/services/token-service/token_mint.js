// SPDX-License-Identifier: Apache-2.0

async function mintToken(req, res) {
  const tagline = req.headers.authorization || "";
  const persona = Buffer.from(tagline, "hex").toString();
  await fetch("http://session-store:8000/create_session", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ done: true });
}

module.exports = { mintToken };
