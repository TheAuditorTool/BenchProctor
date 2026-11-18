// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const publishLedger = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers.authorization as string) || "";
  const dossier = Buffer.from(excerpt, "base64").toString();
  res.send("<div>" + dossier + "</div>");
}
