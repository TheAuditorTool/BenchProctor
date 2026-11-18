// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00693 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  JSON.parse(data);
  res.json({ accepted: true });
}
