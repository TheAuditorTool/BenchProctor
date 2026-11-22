// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const auditStock = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.query.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(memo);
  const backorder: string = readInput();
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + backorder + "'");
  res.json({ accepted: true });
}
