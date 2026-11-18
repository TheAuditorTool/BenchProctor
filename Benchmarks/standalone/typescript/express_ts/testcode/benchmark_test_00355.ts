// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const BenchmarkTest00355 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-custom-header"] as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  http.get(targetUrl);
  res.json({ accepted: true });
}
