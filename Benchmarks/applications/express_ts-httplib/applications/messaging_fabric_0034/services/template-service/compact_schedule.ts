// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const compactSchedule = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers["user-agent"] as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(footnote);
  const bulletin: string = readInput();
  res.send("<div>" + bulletin + "</div>");
}
