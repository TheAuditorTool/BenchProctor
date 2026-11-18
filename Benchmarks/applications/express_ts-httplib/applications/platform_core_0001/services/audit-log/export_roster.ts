// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const exportRoster = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.headers.authorization as string) || "";
  const persona = Buffer.from(tagline, "base64").toString();
  res.send("<div>" + persona + "</div>");
}
