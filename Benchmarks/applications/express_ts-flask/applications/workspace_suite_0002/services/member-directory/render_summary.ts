// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const renderSummary = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body.payload as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const heading: string = normalize(transcript);
  if (!/^(asc|desc|name|created)$/.test(String(heading))) { res.status(400).json({error:"invalid"}); return; }
  const passage = heading;
  childProcess.execSync("echo " + passage);
  res.json({ accepted: true });
}
