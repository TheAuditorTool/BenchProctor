// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const resolveIndex = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.headers.authorization as string) || "";
  const ledger = Buffer.from(subtitle, "base64").toString();
  res.send("<div>" + ledger + "</div>");
}
