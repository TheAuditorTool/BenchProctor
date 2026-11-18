// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const annotateLedger = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.authorization as string) || "";
  const inquiry = Buffer.from(phrase, "base64").toString();
  res.send("<div>" + inquiry + "</div>");
}
