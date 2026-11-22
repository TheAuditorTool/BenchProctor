// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00055 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.host as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  req.session.data = String(data);
  res.json({ accepted: true });
}
