// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildReport = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(phrase);
  const backorder: string = readInput();
  res.send("<div>" + backorder + "</div>");
}
