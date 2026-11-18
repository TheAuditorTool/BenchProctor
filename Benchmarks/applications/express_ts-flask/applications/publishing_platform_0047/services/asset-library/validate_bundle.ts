// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const validateBundle = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.body.payload as string) || "";
  const payload = { get value() { return synopsis; } };
  const byline = payload.value;
  let _host = "";
  try { _host = new URL(String(byline)).hostname; } catch (e) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const _addr = (await require("dns").promises.lookup(_host)).address;
  if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const addendum = byline;
  http.get(addendum);
  res.json({ accepted: true });
}
