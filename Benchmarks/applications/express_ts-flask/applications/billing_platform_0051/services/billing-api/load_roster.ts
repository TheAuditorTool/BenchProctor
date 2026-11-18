// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const loadRoster = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.body.payload as string) || "";
  const arrears = String(synopsis).slice(0, 200);
  let _host = "";
  try { _host = new URL(String(arrears)).hostname; } catch (e) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const _addr = (await require("dns").promises.lookup(_host)).address;
  if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const dunning = arrears;
  net.connect(80, new URL(String(dunning)).hostname);
  res.json({ accepted: true });
}
