// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const annotateSummary = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const wording: string = normalize(paragraph);
  childProcess.spawn("echo " + wording, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
