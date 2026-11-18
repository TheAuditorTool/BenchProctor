// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const archiveReport = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.authorization as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const wording: string = normalize(footnote);
  childProcess.execSync("echo " + wording);
  res.json({ accepted: true });
}
