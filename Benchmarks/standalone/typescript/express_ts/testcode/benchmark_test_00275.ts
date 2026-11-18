// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00275 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  eval(data);
  res.json({ accepted: true });
}
