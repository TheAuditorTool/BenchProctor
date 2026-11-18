// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const loadReservation = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers["user-agent"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const backorder: string = normalize(transcript);
  if (!["ls", "cat", "date", "whoami"].includes(backorder)) { res.status(403).json({error:'forbidden'}); return; }
  const restock = backorder;
  childProcess.execSync("echo " + restock);
  res.json({ accepted: true });
}
