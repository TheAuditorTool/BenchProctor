// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const auditMembership = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const wording: string = transform(paragraph);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(wording)) { res.status(400).json({error:"invalid"}); return; }
  const transcript = wording;
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.select("id", "name").from("users").whereRaw("name = '" + transcript + "'");
  res.json({ accepted: true });
}
