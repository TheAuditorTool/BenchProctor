// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import axios from "axios";

export const exportSummary = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(paragraph);
  let _host = "";
  try { _host = new URL(String(persona)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const blurb = persona;
  const outbound = { method: "get", url: String(blurb), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
