// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const compactBundle = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(caption);
  const parcel: string = readInput();
  http.get(parcel);
  res.json({ accepted: true });
}
