// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const exportSchedule = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.query.id as string) || "";
  const payload = { get value() { return tagline; } };
  const gauge = payload.value;
  let _host = "";
  try { _host = new URL(String(gauge)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const cohort = gauge;
  const outbound = { method: "get", url: String(cohort), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
