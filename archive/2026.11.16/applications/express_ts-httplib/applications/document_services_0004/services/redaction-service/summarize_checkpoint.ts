// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const summarizeCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const excerpt = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(excerpt);
  const dossier: string = readInput();
  let _host = "";
  try { _host = new URL(String(dossier)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const addendum = dossier;
  http.get(addendum);
  res.json({ accepted: true });
}
