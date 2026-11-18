// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("retry-service")
export class NormalizeHeader {
  @Post("normalizeHeader")
  async normalizeHeader(@Req() req: Request): Promise<unknown> {
    const synopsis = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(synopsis);
    const resolved = path.resolve("/var/app/data", handshake);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const memo = resolved;
    const fileContent = fs.readFileSync(memo, "utf8");
    return fileContent;
  }
}
