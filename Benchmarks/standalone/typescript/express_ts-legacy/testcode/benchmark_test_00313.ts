// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00313 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  return res.status(302).set("Location", String(data)).end();
}
