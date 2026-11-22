// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import axios from "axios";

export const archiveSnapshot = async (req: Request, res: Response): Promise<void> => {
  const caption = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value: string): string { return value.normalize("NFC"); }
  const synopsis: string = normalize(caption);
  let _host = "";
  try { _host = new URL(String(synopsis)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const snippet = synopsis;
  const outbound = { method: "get", url: String(snippet), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
