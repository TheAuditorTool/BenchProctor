// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const collectBundle = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.multipart_field as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(summary);
  const cohort: string = readInput();
  let _host = "";
  try { _host = new URL(String(cohort)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const gauge = cohort;
  http.get(gauge);
  res.json({ accepted: true });
}
