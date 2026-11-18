// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const BenchmarkTest00036 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const data = userInput != null ? userInput : '';
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  net.connect(80, new URL(String(targetUrl)).hostname);
  res.json({ accepted: true });
}
