// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const validateWindow = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.query.id as string) || "";
  const payload = { get value() { return headline; } };
  const remittance = payload.value;
  let _host = "";
  try { _host = new URL(String(remittance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dunning = remittance;
  const outbound = { method: "get", url: String(dunning), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
