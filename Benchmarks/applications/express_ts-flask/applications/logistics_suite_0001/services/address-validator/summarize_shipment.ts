// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const summarizeShipment = async (req: Request, res: Response): Promise<void> => {
  const quotation = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(quotation).split(',')) { parts.push(token); }
  const parcel: string = parts.join(',');
  res.send("<div>" + parcel + "</div>");
}
