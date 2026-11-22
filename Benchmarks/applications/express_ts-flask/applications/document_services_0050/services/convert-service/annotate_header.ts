// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { createClient } from "redis";

export const annotateHeader = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const citation = (await _cache.get("user_data")) || "";
  let dossier;
  try { dossier = JSON.parse(citation).value || citation; }
  catch (e) { dossier = citation; }
  JSON.parse(dossier);
  res.json({ accepted: true });
}
