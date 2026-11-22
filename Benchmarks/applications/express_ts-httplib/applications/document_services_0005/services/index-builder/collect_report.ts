// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const collectReport = async (req: Request, res: Response): Promise<void> => {
  const footnote = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const addendum = footnote != null ? footnote : '';
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dossier = addendum;
  http.get(dossier);
  res.json({ accepted: true });
}
