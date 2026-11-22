// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const storeArchive = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.query.id as string) || "";
  const [addendum] = String(wording).split(',');
  await fetch("http://document-api:8000/upload_document", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
  res.json({ accepted: true });
}
