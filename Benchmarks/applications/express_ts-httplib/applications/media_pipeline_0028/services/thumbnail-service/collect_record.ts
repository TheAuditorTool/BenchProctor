// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const collectRecord = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body as string) || "";
  const rendition = citation != null ? citation : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(rendition)) { res.status(400).json({error:"invalid"}); return; }
  const montage = rendition;
  res.send("<div>" + montage + "</div>");
}
