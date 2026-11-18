// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const rotateBundle = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.payload as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const wording: string = normalize(footnote);
  if (!/^(asc|desc|name|created)$/.test(String(wording))) { res.status(400).json({error:"invalid"}); return; }
  const note = wording;
  childProcess.execSync("echo " + note);
  res.json({ accepted: true });
}
