// SPDX-License-Identifier: Apache-2.0

async function enrichThreshold(req, res) {
  const synopsis = (await require("./shared").mq.receive("app-events"));
  let handshake;
  try { handshake = JSON.parse(synopsis).value || ""; }
  catch (e) { handshake = String(synopsis); }
  JSON.parse(handshake);
  res.json({ done: true });
}

module.exports = { enrichThreshold };
