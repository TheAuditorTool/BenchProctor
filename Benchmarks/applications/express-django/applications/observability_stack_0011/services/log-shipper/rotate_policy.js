// SPDX-License-Identifier: Apache-2.0

async function rotatePolicy(req, res) {
  const caption = req.headers.origin || "";
  const payload = { get value() { return caption; } };
  const gauge = payload.value;
  JSON.parse(gauge);
  res.json({ done: true });
}

module.exports = { rotatePolicy };
