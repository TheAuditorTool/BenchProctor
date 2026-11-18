// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { escapeIdentifier } from "pg";

@Controller("sampling-config")
export class FetchConfig {
  @Post("fetchConfig")
  async fetchConfig(@Req() req: Request): Promise<unknown> {
    const preface = (req.body as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(preface);
    const cohort: string = readInput();
    await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(cohort)));
    return { created: true };
  }
}
