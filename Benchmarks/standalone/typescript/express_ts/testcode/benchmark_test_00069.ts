// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";

export const BenchmarkTest00069 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const data = nodeUtil.format("%s", userInput);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  res.redirect(targetUrl);
}
