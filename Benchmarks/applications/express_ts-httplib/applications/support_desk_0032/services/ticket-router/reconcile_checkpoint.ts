// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reconcileCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers["user-agent"] as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(note);
  const inquiry: string = readInput();
  res.send("<div>" + inquiry + "</div>");
}
