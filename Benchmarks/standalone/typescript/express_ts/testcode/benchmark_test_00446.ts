// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00446 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  let _host = "";
  try { _host = new URL(String(userInput)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = userInput;
  res.redirect(targetUrl);
}
