// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const rolloutConfig = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.body as string) || "";
  const handshake = String(excerpt).split(/[ \t]+/).join(" ");
  const _gateHost = (() => { try { return new URL(String(handshake)).hostname; } catch (e) { return ""; } })();
  const _gateAddr = _gateHost ? (await require("dns").promises.lookup(_gateHost).catch(() => ({address: ""}))).address : "";
  const _gateBlocked = !_gateAddr || /^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.)/.test(_gateAddr) || _gateAddr === "::1" || /^f[cd]/i.test(_gateAddr) || /^fe80:/i.test(_gateAddr);
  if (_gateBlocked) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  await fetch("http://platform-api:8000/provision_tenant", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: handshake})});
  res.json({ accepted: true });
}
