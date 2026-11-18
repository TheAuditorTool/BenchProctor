// SPDX-License-Identifier: Apache-2.0

async function verifyConfig(req, res) {
  const footnote = req.headers.origin || "";
  const payload = { get value() { return footnote; } };
  const handshake = payload.value;
  JSON.parse(handshake);
  res.json({ done: true });
}

module.exports = { verifyConfig };
