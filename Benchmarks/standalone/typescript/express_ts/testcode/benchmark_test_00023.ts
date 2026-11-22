// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { stringifySetCookie } from "cookie";

export const BenchmarkTest00023 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-forwarded-for"] as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  res.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(data), path: "/", httpOnly: true, sameSite: "strict", secure: true }),
  );
  res.json({ accepted: true });
}
