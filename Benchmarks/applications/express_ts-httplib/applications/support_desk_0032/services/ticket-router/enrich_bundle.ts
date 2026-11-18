// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const enrichBundle = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body.multipart_field as string) || "";
  const transform = (v: string): string => v.trim();
  const inquiry: string = transform(note);
  const grievance = "/var/app/data/" + path.basename(inquiry);
  fs.unlinkSync(grievance);
  res.json({ accepted: true });
}
