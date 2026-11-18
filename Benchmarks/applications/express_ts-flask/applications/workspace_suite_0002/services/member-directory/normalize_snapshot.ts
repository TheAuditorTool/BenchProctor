// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const normalizeSnapshot = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body.payload as string) || "";
  const heading = String(transcript).slice(0, 200);
  let _host = "";
  try { _host = new URL(String(heading)).hostname; } catch (e) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const _addr = (await require("dns").promises.lookup(_host)).address;
  if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const passage = heading;
  net.connect(80, new URL(String(passage)).hostname);
  res.json({ accepted: true });
}
