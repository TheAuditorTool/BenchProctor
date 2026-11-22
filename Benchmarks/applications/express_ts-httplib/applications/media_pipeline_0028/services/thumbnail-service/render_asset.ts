// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const renderAsset = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.host as string) || "";
  const transform = (v: string): string => v.trim();
  const rendition: string = transform(citation);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(rendition)) { res.status(400).json({error:"invalid"}); return; }
  const montage = rendition;
  const fileContent = fs.readFileSync("/var/app/data/" + montage, "utf8");
  res.send(fileContent);
}
