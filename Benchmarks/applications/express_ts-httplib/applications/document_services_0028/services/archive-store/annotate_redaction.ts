// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const annotateRedaction = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body.multipart_field as string) || "";
  const addendum = decodeURIComponent(note);
  http.get(addendum);
  res.json({ accepted: true });
}
