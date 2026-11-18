// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const indexMetadata = async (req: Request, res: Response): Promise<void> => {
  const passage = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(passage);
  const montage: string = readInput();
  await fetch("http://thumbnail-service:8000/render_thumbnail", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: montage})});
  res.json({ accepted: true });
}
