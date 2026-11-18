// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const validateBundle = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers["x-custom-header"] as string) || "";
  const formData = Object.freeze({ payload: excerpt });
  const gauge = formData.payload;
  let _host = "";
  try { _host = new URL(String(gauge)).hostname; } catch (e) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const _addr = (await require("dns").promises.lookup(_host)).address;
  if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const cohort = gauge;
  net.connect(80, new URL(String(cohort)).hostname);
  res.json({ accepted: true });
}
