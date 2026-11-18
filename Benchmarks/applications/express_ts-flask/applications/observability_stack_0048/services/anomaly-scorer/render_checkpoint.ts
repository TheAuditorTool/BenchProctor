// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const renderCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const excerpt = process.env.TELEMETRY_INPUT_0048 || "";
  const transform = (v: string): string => v.trim();
  const gauge: string = transform(excerpt);
  childProcess.execSync("echo " + gauge);
  res.json({ accepted: true });
}
