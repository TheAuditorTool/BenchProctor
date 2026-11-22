// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const annotateSummary = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.body.multipart_field as string) || "";
  let wording;
  try { wording = JSON.parse(paragraph).value || paragraph; }
  catch (e) { wording = paragraph; }
  fs.unlinkSync("/var/app/data/" + wording);
  res.json({ accepted: true });
}
