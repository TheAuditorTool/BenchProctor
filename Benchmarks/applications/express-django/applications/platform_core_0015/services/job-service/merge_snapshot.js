// SPDX-License-Identifier: Apache-2.0

async function mergeSnapshot(req, res) {
  const note = req.headers.origin || "";
  const payload = { get value() { return note; } };
  const handshake = payload.value;
  JSON.parse(handshake);
  res.json({ done: true });
}

module.exports = { mergeSnapshot };
