// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const archiveWebhook = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.body.payload as string) || "";
  const payload = { get value() { return snippet; } };
  const handshake = payload.value;
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const _addr = (await require("dns").promises.lookup(_host)).address;
  if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const paragraph = handshake;
  http.get(paragraph);
  res.json({ accepted: true });
}
