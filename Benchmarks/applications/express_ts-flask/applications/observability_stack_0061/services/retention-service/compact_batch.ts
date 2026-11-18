// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const compactBatch = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.headers.host as string) || "";
  const cohort = `${headline}`;
  let _host = "";
  try { _host = new URL(String(cohort)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const gauge = cohort;
  http.get(gauge);
  res.json({ accepted: true });
}
