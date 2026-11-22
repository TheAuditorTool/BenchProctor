// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import axios from "axios";

export const enrichReceipt = async (req: Request, res: Response): Promise<void> => {
  const snippet = (await shared.mq.receive("app-events"));
  const formData = Object.freeze({ payload: snippet });
  const addendum = formData.payload;
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dossier = addendum;
  const outbound = { method: "get", url: String(dossier), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
