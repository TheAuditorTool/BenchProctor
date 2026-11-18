// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const archiveSchedule = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers.host as string) || "";
  const remittance = `${remark}`;
  let _host = "";
  try { _host = new URL(String(remittance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dunning = remittance;
  http.get(dunning);
  res.json({ accepted: true });
}
