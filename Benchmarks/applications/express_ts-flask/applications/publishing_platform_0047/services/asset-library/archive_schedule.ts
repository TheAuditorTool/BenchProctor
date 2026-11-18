// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archiveSchedule = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(synopsis).split(',')) { parts.push(token); }
  const byline: string = parts.join(',');
  res.send("<div>" + byline + "</div>");
}
