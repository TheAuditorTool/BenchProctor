// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildRecord = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers.authorization as string) || "";
  const transform = (v: string): string => v.trim();
  const parcel: string = transform(transcript);
  res.send("<div>" + parcel + "</div>");
}
