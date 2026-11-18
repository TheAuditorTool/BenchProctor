// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const resolveHeader = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers["x-custom-header"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const cohort: string = normalize(summary);
  childProcess.execSync("echo " + cohort);
  res.json({ accepted: true });
}
