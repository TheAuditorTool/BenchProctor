// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const auditBatch = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.cookies?.session_token as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(heading);
  res.send(shared.escapeHtml(handshake));
}
