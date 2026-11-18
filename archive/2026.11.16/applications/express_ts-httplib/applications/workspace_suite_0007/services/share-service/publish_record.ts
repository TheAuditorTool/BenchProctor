// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const publishRecord = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(summary);
  const subtitle: string = readInput();
  res.send("<div>" + subtitle + "</div>");
}
