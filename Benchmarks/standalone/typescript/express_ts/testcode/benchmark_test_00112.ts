// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { stringifySetCookie } from "cookie";

export const BenchmarkTest00112 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  res.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(userInput), path: "/", httpOnly: true, sameSite: "strict" }),
  );
  res.json({ accepted: true });
}
