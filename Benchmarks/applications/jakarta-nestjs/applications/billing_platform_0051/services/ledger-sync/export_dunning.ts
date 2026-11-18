// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("ledger-sync")
export class ExportDunning {
  @Post("exportDunning")
  async exportDunning(@Req() req: Request): Promise<unknown> {
    const synopsis = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const transform = (v: string): string => v.trim();
    const arrears: string = transform(synopsis);
    const resolved = path.resolve("/var/app/data", arrears);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const dunning = resolved;
    const fileContent = fs.readFileSync(dunning, "utf8");
    return fileContent;
  }
}
