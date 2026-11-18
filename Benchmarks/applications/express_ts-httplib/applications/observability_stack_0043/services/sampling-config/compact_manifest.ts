// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const compactManifest = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers["x-custom-header"] as string) || "";
  const transform = (v: string): string => v.trim();
  const gauge: string = transform(note);
  childProcess.execSync("echo " + gauge);
  res.json({ accepted: true });
}
