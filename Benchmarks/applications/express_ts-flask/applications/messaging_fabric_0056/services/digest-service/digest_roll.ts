// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const rollDigest = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(footnote);
  const bulletin: string = readInput();
  await fetch("http://presence-service:8000/update_presence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ accepted: true });
}
