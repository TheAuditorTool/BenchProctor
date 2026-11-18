// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";

export const archiveRoster = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers["user-agent"] as string) || "";
  const handshake = nodeUtil.format("%s", excerpt);
  res.send("<div>" + handshake + "</div>");
}
