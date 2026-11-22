// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const enrichReport = async (req: Request, res: Response): Promise<void> => {
  const excerpt = process.env.TELEMETRY_INPUT_0054 || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const cohort: string = normalize(excerpt);
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.select("id", "name").from("users").whereRaw("name = '" + cohort + "'");
  res.json({ accepted: true });
}
