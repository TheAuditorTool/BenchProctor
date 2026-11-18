// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const collectRecord = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(summary);
  const restock: string = readInput();
  res.send("<div>" + restock + "</div>");
}
