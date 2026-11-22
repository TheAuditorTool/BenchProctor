// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const verifyBundle = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(transcript);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(consignment)) { res.status(400).json({error:"invalid"}); return; }
  const parcel = consignment;
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.select("id", "name").from("users").whereRaw("name = '" + parcel + "'");
  res.json({ accepted: true });
}
