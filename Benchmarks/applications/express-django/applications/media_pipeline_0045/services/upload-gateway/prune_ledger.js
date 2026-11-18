// SPDX-License-Identifier: Apache-2.0

async function pruneLedger(req, res) {
  const notice = req.headers.origin || "";
  const payload = { get value() { return notice; } };
  const rendition = payload.value;
  JSON.parse(rendition);
  res.json({ done: true });
}

module.exports = { pruneLedger };
