// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const auditSchedule = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.body.multipart_field as string) || "";
  let gauge;
  try { gauge = JSON.parse(tagline).value || tagline; }
  catch (e) { gauge = tagline; }
  fs.unlinkSync("/var/app/data/" + gauge);
  res.json({ accepted: true });
}
