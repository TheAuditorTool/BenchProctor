// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import axios from "axios";

export const pruneSummary = async (req: Request, res: Response): Promise<void> => {
  const transcript = (await shared.mq.receive("app-events"));
  const formData = Object.freeze({ payload: transcript });
  const consignment = formData.payload;
  let _host = "";
  try { _host = new URL(String(consignment)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const parcel = consignment;
  const outbound = { method: "get", url: String(parcel), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
