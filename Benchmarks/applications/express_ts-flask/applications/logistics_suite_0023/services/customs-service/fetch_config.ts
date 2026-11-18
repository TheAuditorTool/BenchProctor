// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const fetchConfig = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(caption);
  const parcel: string = readInput();
  res.send("<div>" + parcel + "</div>");
}
