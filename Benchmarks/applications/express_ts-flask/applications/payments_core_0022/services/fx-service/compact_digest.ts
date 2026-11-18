// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const compactDigest = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.params.id as string) || "";
  const ledger = decodeURIComponent(subject);
  res.send("<div>" + ledger + "</div>");
}
