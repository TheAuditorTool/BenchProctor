// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const rollDigest = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.headers.authorization as string) || "";
  const transform = (v: string): string => v.trim();
  const bulletin: string = transform(paragraph);
  await fetch("http://presence-service:8080/update_presence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ accepted: true });
}
