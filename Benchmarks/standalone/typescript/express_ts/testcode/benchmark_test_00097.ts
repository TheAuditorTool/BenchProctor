// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { stringifySetCookie } from "cookie";

export const BenchmarkTest00097 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  res.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(data), path: "/", httpOnly: true, sameSite: "strict" }),
  );
  res.json({ accepted: true });
}
