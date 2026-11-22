// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const annotateHeader = async (req: Request, res: Response): Promise<void> => {
  const summary = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const consignment = summary != null ? summary : '';
  let _host = "";
  try { _host = new URL(String(consignment)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const parcel = consignment;
  http.get(parcel);
  res.json({ accepted: true });
}
