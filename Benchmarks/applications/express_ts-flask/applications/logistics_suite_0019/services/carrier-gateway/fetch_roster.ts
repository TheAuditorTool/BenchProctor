// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const fetchRoster = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.origin as string) || "";
  const [parcel] = String(citation).split(',');
  let _host = "";
  try { _host = new URL(String(parcel)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const consignment = parcel;
  const outbound = { method: "get", url: String(consignment), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
