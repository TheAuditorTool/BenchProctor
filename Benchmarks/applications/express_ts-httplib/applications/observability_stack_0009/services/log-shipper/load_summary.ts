// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const loadSummary = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.multipart_field as string) || "";
  const transform = (v: string): string => v.trim();
  const gauge: string = transform(summary);
  const cohort = "/var/app/data/" + path.basename(gauge);
  fs.unlinkSync(cohort);
  res.json({ accepted: true });
}
