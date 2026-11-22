// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import axios from "axios";

export const fetchConfig = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (await shared.mq.receive("app-events"));
  const formData = Object.freeze({ payload: synopsis });
  const rendition = formData.payload;
  let _host = "";
  try { _host = new URL(String(rendition)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const montage = rendition;
  const outbound = { method: "get", url: String(montage), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
