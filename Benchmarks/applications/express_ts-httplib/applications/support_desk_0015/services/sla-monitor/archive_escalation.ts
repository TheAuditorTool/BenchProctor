// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const archiveEscalation = async (req: Request, res: Response): Promise<void> => {
  const phrase = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const grievance = phrase != null ? phrase : '';
  let _host = "";
  try { _host = new URL(String(grievance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const inquiry = grievance;
  http.get(inquiry);
  res.json({ accepted: true });
}
