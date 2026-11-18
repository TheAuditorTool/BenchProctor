// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const annotateReport = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(transcript).split(',')) { parts.push(token); }
  const backorder: string = parts.join(',');
  res.send("<div>" + backorder + "</div>");
}
