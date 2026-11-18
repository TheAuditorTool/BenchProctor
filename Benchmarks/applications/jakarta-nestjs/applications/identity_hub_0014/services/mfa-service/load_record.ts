// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("mfa-service")
export class LoadRecord {
  @Post("loadRecord")
  async loadRecord(@Req() req: Request): Promise<unknown> {
    const snippet = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const transform = (v: string): string => v.trim();
    const persona: string = transform(snippet);
    const resolved = path.resolve("/var/app/data", persona);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const synopsis = resolved;
    const fileContent = fs.readFileSync(synopsis, "utf8");
    return fileContent;
  }
}
