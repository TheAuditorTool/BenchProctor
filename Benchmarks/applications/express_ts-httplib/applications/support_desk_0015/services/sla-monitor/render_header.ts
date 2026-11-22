// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import axios from "axios";

export const renderHeader = async (req: Request, res: Response): Promise<void> => {
  const phrase = (await shared.mq.receive("app-events"));
  const formData = Object.freeze({ payload: phrase });
  const grievance = formData.payload;
  let _host = "";
  try { _host = new URL(String(grievance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const inquiry = grievance;
  const outbound = { method: "get", url: String(inquiry), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
