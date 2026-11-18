// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const collectManifest = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.authorization as string) || "";
  const voucher = Buffer.from(heading, "base64").toString();
  res.send("<div>" + voucher + "</div>");
}
