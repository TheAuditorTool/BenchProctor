// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const mergeConfig = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.multipart_field as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(remark);
  const remittance: string = readInput();
  let _host = "";
  try { _host = new URL(String(remittance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dunning = remittance;
  http.get(dunning);
  res.json({ accepted: true });
}
