// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const createSession = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.body.field as string) || "";
  const persona = decodeURIComponent(excerpt);
  await fetch("http://directory-sync:8000/sync_directory", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ accepted: true });
}
