// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const resolveWindow = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers["x-custom-header"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const gauge: string = normalize(caption);
  childProcess.execSync("echo " + gauge);
  res.json({ accepted: true });
}
