// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reconcileCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const note = (req.params.id as string) || "";
  const inquiry = decodeURIComponent(note);
  res.send("<div>" + inquiry + "</div>");
}
