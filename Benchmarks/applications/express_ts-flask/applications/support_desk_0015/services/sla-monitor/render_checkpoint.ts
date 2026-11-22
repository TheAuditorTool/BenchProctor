// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const renderCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.query.id as string) || "";
  const payload = { get value() { return phrase; } };
  const grievance = payload.value;
  let _host = "";
  try { _host = new URL(String(grievance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const inquiry = grievance;
  const outbound = { method: "get", url: String(inquiry), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
