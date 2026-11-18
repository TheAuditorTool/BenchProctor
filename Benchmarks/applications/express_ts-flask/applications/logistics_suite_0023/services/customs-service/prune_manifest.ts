// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const pruneManifest = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.host as string) || "";
  const parcel = `${caption}`;
  let _host = "";
  try { _host = new URL(String(parcel)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const consignment = parcel;
  http.get(consignment);
  res.json({ accepted: true });
}
