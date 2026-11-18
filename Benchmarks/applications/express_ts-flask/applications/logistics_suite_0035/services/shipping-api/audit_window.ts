// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const auditWindow = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.authorization as string) || "";
  const transform = (v: string): string => v.trim();
  const parcel: string = transform(phrase);
  res.send("<div>" + parcel + "</div>");
}
