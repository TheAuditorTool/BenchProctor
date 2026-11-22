// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import axios from "axios";

export const renderRecord = async (req: Request, res: Response): Promise<void> => {
  const transcript = (await shared.mq.receive("app-events"));
  const formData = Object.freeze({ payload: transcript });
  const addendum = formData.payload;
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const byline = addendum;
  const outbound = { method: "get", url: String(byline), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
