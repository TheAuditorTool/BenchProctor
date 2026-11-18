// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00018 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  res.redirect(data);
}
