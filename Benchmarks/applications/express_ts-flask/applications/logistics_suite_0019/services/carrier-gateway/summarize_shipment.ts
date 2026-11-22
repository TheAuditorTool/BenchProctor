// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const summarizeShipment = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body.payload as string) || "";
  const tokens = String(citation).split(',').filter((t) => t.length > 0);
  const parcel = tokens.join(' ');
  res.send("<div>" + parcel + "</div>");
}
