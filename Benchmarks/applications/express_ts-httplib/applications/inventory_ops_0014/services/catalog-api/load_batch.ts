// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import axios from "axios";

export const loadBatch = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (await shared.mq.receive("app-events"));
  const formData = Object.freeze({ payload: excerpt });
  const restock = formData.payload;
  let _host = "";
  try { _host = new URL(String(restock)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const backorder = restock;
  const outbound = { method: "get", url: String(backorder), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
