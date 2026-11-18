// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.body as string) || "";
  const parts: string[] = [];
  for (const token of String(excerpt).split(',')) { parts.push(token); }
  const gauge: string = parts.join(',');
  res.send("<div>" + gauge + "</div>");
}
